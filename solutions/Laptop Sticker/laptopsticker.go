package main

import "fmt"

func main() {
	var wc, hc, ws, hs int

	fmt.Scanln(&wc, &hc, &ws, &hs)

	if wc-ws >= 2 && hc-hs >= 2 {
		fmt.Println(1)
	} else {
		fmt.Println(0)
	}
}