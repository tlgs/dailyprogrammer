// 11/04/2019
package main

import "fmt"

func main() {
	var name, age, username string
	fmt.Print("name: ")
	fmt.Scanln(&name)
	fmt.Print("age: ")
	fmt.Scanln(&age)
	fmt.Print("reddit username: ")
	fmt.Scanln(&username)

	fmt.Printf("your name is %s, you are %s years old and your reddit username is /u/%s",
		name, age, username)
}
