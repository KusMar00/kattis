package main

import "fmt"

func main() {
	var n int
	fmt.Scanln(&n)
	var time int

	if n%2 != 0 {
		fmt.Println("still running")
		return
	}
	
	for i:=0; i<n; i+=2 {
		var t1, t2 int
		fmt.Scanln(&t1)
		fmt.Scanln(&t2)
		time += t2-t1
	}

	fmt.Println(time)
}