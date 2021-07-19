package main

import "fmt"

func lettersum(s string) int {
	t := 0
	for _, c := range []byte(s) {
		t += int(c - 96)
	}
	return t
}

func main() {
	fmt.Println(`lettersum("") => `, lettersum(""))
	fmt.Println(`lettersum("a") => `, lettersum("a"))
	fmt.Println(`lettersum("z") => `, lettersum("z"))
	fmt.Println(`lettersum("cab") => `, lettersum("cab"))
	fmt.Println(`lettersum("excellent") => `, lettersum("excellent"))
	fmt.Println(`lettersum("microspectrophotometries") => `, lettersum("microspectrophotometries"))
}
