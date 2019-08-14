// 14/08/2019
package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

type node struct {
	head  int
	alpha string
}

type array []node

func (a *array) push(x node) {
	*a = append(*a, x)
}

func (a *array) pop() node {
	s := len(*a) - 1
	x := (*a)[s]
	*a = (*a)[:s]
	return x
}

var morse = map[string]string{
	".-": "a", "-...": "b",
	"-.-.": "c", "-..": "d",
	".": "e", "..-.": "f",
	"--.": "g", "....": "h",
	"..": "i", ".---": "j",
	"-.-": "k", ".-..": "l",
	"--": "m", "-.": "n",
	"---": "o", ".--.": "p",
	"--.-": "q", ".-.": "r",
	"...": "s", "-": "t",
	"..-": "u", "...-": "v",
	".--": "w", "-..-": "x",
	"-.--": "y", "--..": "z",
}

func smalpha(seq string) (string, error) {
	stack := make(array, 0, 1<<10)
	for i := 1; i < 5; i++ {
		x, ok := morse[seq[:i]]
		if ok {
			stack.push(node{i, x})
		}
	}

	for len(stack) > 0 {
		n := stack.pop()
		for i := 1; i < 5; i++ {
			if n.head+i > len(seq) {
				break
			}
			sub := seq[n.head : n.head+i]
			x, ok := morse[sub]
			if ok && !strings.Contains(n.alpha, x) {
				nx := node{n.head + i, n.alpha + x}
				if len(nx.alpha) == 26 {
					return nx.alpha, nil
				}
				stack.push(nx)
			}
		}
	}

	return "", fmt.Errorf(seq, "no alphabet found")
}

func main() {
	start := time.Now()
	scanner := bufio.NewScanner(os.Stdin)
	for i := 0; scanner.Scan(); i++ {
		if _, err := smalpha(scanner.Text()); err != nil {
			fmt.Fprintln(os.Stderr, err)
		}
	}
	if err := scanner.Err(); err != nil {
		fmt.Fprintln(os.Stderr, err)
	}
	fmt.Println(time.Since(start))
}
