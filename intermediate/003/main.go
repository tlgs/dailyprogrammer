// 06/05/2019
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func buildCiphertext(key string) []rune {
	key = strings.ToUpper(key)
	lookup := make(map[rune]bool, 26)
	alphabet := make([]rune, 0, 26)

	for _, v := range key {
		if _, ok := lookup[v]; ok {
			continue
		} else {
			lookup[v] = true
			alphabet = append(alphabet, v)
		}
	}

	for c := 'A'; c <= 'Z'; c++ {
		if _, ok := lookup[c]; ok {
			continue
		} else {
			lookup[c] = true
			alphabet = append(alphabet, c)
		}
	}

	return alphabet
}

// Mixed Alphabet Substitution written out in blocks
func masEncryption(text string, ciphertext []rune, n int) string {
	text = strings.ToUpper(text)
	t := []rune(text)

	r := make([]rune, 0, len(t)+len(t)/n+1)

	count := 0
	for _, v := range t {
		if v < 'A' || v > 'Z' {
			continue
		}

		r = append(r, rune(ciphertext[v-'A']))
		count++

		if count%n == 0 {
			r = append(r, ' ')
		}
	}

	// if last block is not filled -> fill with 'A's
	if count%n != 0 {
		for i := 0; i < n-(count%n); i++ {
			r = append(r, 'A')
		}
	}

	return string(r)
}

func main() {
	var key, text string

	fmt.Print("key: ")
	fmt.Scanln(&key)

	scanner := bufio.NewScanner(os.Stdin)
	for {
		fmt.Print(">> ")
		scanner.Scan()
		text = scanner.Text()
		fmt.Println(masEncryption(text, buildCiphertext(key), 5))
	}
}
