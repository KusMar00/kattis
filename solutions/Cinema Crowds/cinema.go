package main

import "fmt"

func main() {
	var seats, groups, counter, tmpGroup int
	fmt.Scanln(&seats, &groups)
	
	
	for i:=0; i<groups; i++ {
		fmt.Scan(&tmpGroup)
		if (seats - tmpGroup < 0) {
			counter++
		} else {
			seats -= tmpGroup
		}
	}

	fmt.Println(counter)
}