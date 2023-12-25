package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)
	for {
		if (n<1) {
			return
		}
		fmt.Print(n%10)
		n = n/10
	}
	
}