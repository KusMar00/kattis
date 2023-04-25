package main

import (
	"fmt"
	"math"
)

func main() {
	var h, v, result float64
	fmt.Scanln(&h, &v)
	result = h/math.Sin(v/57.29578)

	fmt.Println(int64(result)+1)
}
