package main

import "fmt"

func main() {
	var seats, groups, tmpGroup, counter int
	fmt.Scanln(&seats, &groups)
	
	
	for i:=0; i<groups; i++ {
		fmt.Scan(&tmpGroup)
		seats -= tmpGroup
		if (seats < 0) {
			break
		}
		counter++
	}

	fmt.Println(groups-counter)
	
}