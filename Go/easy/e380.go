// 13/08/2019
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func smorse(word string) string {
	table := "&75+#=)?'8*;$%(92-/\".>,643"
	var morse [32 * 4]byte
	var count uint8
	for _, char := range word {
		v := table[char-'a'] - 32
		var i uint8 = 4
		for ; (v >> i & 1) == 0; i-- {
		}
		for i--; i < 255; i-- {
			if (v >> i & 1) == 1 {
				morse[count] = '.'
			} else {
				morse[count] = '-'
			}
			count++
		}
	}
	return string(morse[:count])
}

func bonus1(words []string) (string, error) {
	m := make(map[string]uint)

	for _, word := range words {
		smorsed := smorse(word)
		if m[smorsed] == 12 {
			return smorsed, nil
		}
		m[smorsed] = m[smorsed] + 1
	}

	return "", fmt.Errorf("no sequence that's code for 13 different words")
}

func bonus2(words []string) (string, error) {
	dashes := strings.Repeat("-", 15)
	for _, word := range words {
		if len(word)*3 < 15 {
			continue
		} else if strings.Contains(smorse(word), dashes) {
			return word, nil
		}
	}

	return "", fmt.Errorf("no smorsed word has 15 dashes in a row")
}

func bonus3(words []string) (string, error) {
	for _, word := range words {
		if len(word) != 21 || word == "counterdemonstrations" {
			continue
		}
		smorsed := smorse(word)
		dashes := strings.Count(smorsed, "-")
		dots := strings.Count(smorsed, ".")
		if dashes == dots {
			return word, nil
		}
	}

	return "", fmt.Errorf("no other 21-letter word is perfectly balanced")
}

func bonus4(words []string) (string, error) {
	for _, word := range words {
		if len(word) != 13 {
			continue
		}
		smorsed := smorse(word)
		f := true
		for i, j := 0, len(smorsed)-1; i < len(smorsed)/2; i, j = i+1, j-1 {
			if smorsed[i] != smorsed[j] {
				f = false
				break
			}
		}
		if f {
			return word, nil
		}
	}

	return "", fmt.Errorf("no 13-letter word encodes to a palindrome")
}

func bonus5(words []string) ([]string, error) {
	seqs := make([]string, len(words))
	for i, word := range words {
		if len(word)*4 < 13 {
			continue
		}
		seqs[i] = smorse(word)
	}

	m := make(map[int]bool)
	for i := 0; i < (1 << 13); i++ {
		m[i] = true
	}
	delete(m, 1092)

	for _, seq := range seqs {
		for i := 0; i < len(seq)-12; i++ {
			x := 0
			for j, char := range seq[i : i+13] {
				if char == '.' {
					x = x | (1 << (12 - uint8(j)))
				}
			}
			delete(m, x)
		}
		if len(m) == 4 {
			r, count := make([]string, 4), 0
			for k := range m {
				var morse [13]byte
				for i := uint8(12); i < 255; i-- {
					if (k >> i & 1) == 1 {
						morse[12-i] = '.'
					} else {
						morse[12-i] = '-'
					}
				}
				r[count], count = string(morse[:]), count+1
			}
			return r, nil
		}
	}

	msg := "no other four 13-character sequences that do not appear in the encoding of any word"
	return []string{""}, fmt.Errorf(msg)
}

func main() {
	words := make([]string, 1<<20)
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; scanner.Scan(); i++ {
		words[i] = scanner.Text()
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
	}

	v, _ := bonus1(words)
	fmt.Println("Bonus 1:", v)

	v, _ = bonus2(words)
	fmt.Println("Bonus 2:", v)

	v, _ = bonus3(words)
	fmt.Println("Bonus 3:", v)

	v, _ = bonus4(words)
	fmt.Println("Bonus 4:", v)

	w, _ := bonus5(words)
	fmt.Println("Bonus 5:", w[0])
	for _, seq := range w[1:] {
		fmt.Println("        ", seq)
	}
}
