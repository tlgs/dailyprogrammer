// 11/04/2019
package main

import "fmt"

func fit1(X, Y, x, y int) int {
	return (X / x) * (Y / y)
}

func fit2(X, Y, x, y int) int {
	a := fit1(X, Y, x, y)
	b := fit1(X, Y, y, x)

	if a >= b {
		return a
	}
	return b
}

func fit3(X, Y, Z, x, y, z int) int {
	rotations := [6]int{
		(X / x) * (Y / y) * (Z / z),
		(X / x) * (Y / z) * (Z / y),
		(X / y) * (Y / x) * (Z / z),
		(X / y) * (Y / z) * (Z / x),
		(X / z) * (Y / x) * (Z / y),
		(X / z) * (Y / y) * (Z / x),
	}

	max := 0
	for _, v := range rotations {
		if v > max {
			max = v
		}
	}
	return max
}

func main() {
	fmt.Println("fit1(25, 18, 6, 5) :", fit1(25, 18, 6, 5))
	fmt.Println("fit1(10, 10, 1, 1) :", fit1(10, 10, 1, 1))
	fmt.Println("fit1(12, 34, 5, 6) :", fit1(12, 34, 5, 6))
	fmt.Println("fit1(12345, 678910, 1112, 1314) :", fit1(12345, 678910, 1112, 1314))
	fmt.Println("fit1(5, 100, 6, 1) :", fit1(5, 100, 6, 1))
	fmt.Println()
	fmt.Println("fit2(25, 18, 6, 5) :", fit2(25, 18, 6, 5))
	fmt.Println("fit2(12, 34, 5, 6) :", fit2(12, 34, 5, 6))
	fmt.Println("fit2(12345, 678910, 1112, 1314) :", fit2(12345, 678910, 1112, 1314))
	fmt.Println("fit2(5, 5, 3, 2) :", fit2(5, 5, 3, 2))
	fmt.Println("fit2(5, 100, 6, 1) :", fit2(5, 100, 6, 1))
	fmt.Println("fit2(5, 5, 6, 1) :", fit2(5, 5, 6, 1))
	fmt.Println()
	fmt.Println("fit3(10, 10, 10, 1, 1, 1) :", fit3(10, 10, 10, 1, 1, 1))
	fmt.Println("fit3(12, 34, 56, 7, 8, 9) :", fit3(12, 34, 56, 7, 8, 9))
	fmt.Println("fit3(123, 456, 789, 10, 11, 12) :", fit3(123, 456, 789, 10, 11, 12))
	fmt.Println("fit3(1234567, 89101112, 13141516, 171819, 202122, 232425):", fit3(1234567, 89101112, 13141516, 171819, 202122, 232425))
}
