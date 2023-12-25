package main

import "fmt"

var n, counter int
var tmp float64

func main() {
	fmt.Scanln(&n)
	for i := 0; i < n; i++ {
		fmt.Scanln(&tmp)
		counter = 0
		for {
			tmp /= 10
			counter++
			if tmp < 1 {
				break
			}
		}
		fmt.Println(counter)
	}
}