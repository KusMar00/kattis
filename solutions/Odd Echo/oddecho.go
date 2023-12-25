package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)

	var tmp string
	for i := 0; i < n; i++ {
		fmt.Scanln(&tmp)
		if i%2 == 0 {
			fmt.Println(tmp)
		}
	}
}