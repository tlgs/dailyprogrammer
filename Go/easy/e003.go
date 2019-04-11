// 11/04/2019
package main

import (
	"bufio"
	"fmt"
	"os"
)

func rot13(s string) string {
	r := []rune(s)
	for i, v := range r {
		if v >= 'a' && v <= 'z' {
			r[i] = 'a' + (v-'a'+13)%26
		} else if v >= 'A' && v <= 'Z' {
			r[i] = 'A' + (v-'A'+13)%26
		}
	}

	return string(r)
}

func main() {
	s := bufio.NewScanner(os.Stdin)
	fmt.Print(">> ")
	s.Scan()
	input := s.Text()
	fmt.Printf("rot13(%s): %s\n", input, rot13(input))
}
