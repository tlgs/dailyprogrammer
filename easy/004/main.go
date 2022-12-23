// 15/04/2019
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	rand.Seed(time.Now().UnixNano())

	const alpha = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	var n, pLength int

	fmt.Print("Password length: ")
	fmt.Scanln(&pLength)
	fmt.Print("Number of passwords: ")
	fmt.Scanln(&n)
	fmt.Println()

	for i := 0; i < n; i++ {
		pw := make([]rune, pLength)
		for j := 0; j < pLength; j++ {
			pw[j] = rune(alpha[rand.Intn(26*2+10)])
		}

		fmt.Println(string(pw))
	}
}
