// 11/04/2019
package main

import "fmt"

func main() {
	var mass, accel float64
	fmt.Print("Mass (m): ")
	fmt.Scanln(&mass)
	fmt.Print("Accelaration (a): ")
	fmt.Scanln(&accel)

	fmt.Println("Force (F = m*a):", (mass * accel))
}
