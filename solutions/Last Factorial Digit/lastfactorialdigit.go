package main

import "fmt"

func main() {
	var c int
	fmt.Scanln(&c)
	
	var n int;
	var digit int = 1
	for i:=0; i<c; i++ {
		fmt.Scanln(&n)
		if (n < 5) {
			for j:=2; j<=n; j++ {
				digit *= j
			}
			digit = digit%10
		} else {
			digit = 0
		}
		fmt.Println(digit)
		digit = 1
	}
}