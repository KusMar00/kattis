package main

import "fmt"

func main() {
	var month string
	var date int

	fmt.Scanln(&month, &date)

	if month == "OCT" && date == 31 {
		fmt.Print("yup")
	} else if month == "DEC" && date == 25 {
		fmt.Print("yup")
	} else {
		fmt.Print("nope")
	}
}