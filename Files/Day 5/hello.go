package main

import (
	"fmt"
)

func main() {

	fmt.Println("Hello, World !")

	x := 69
	y := 55
	sum1 := x + y

	// we can use this methob but it is not preferred.
	fmt.Println("\nNumbers:")
	var a int = 1
	var b int = 222
	var sum2 int = a + b
	fmt.Println("a+b=", sum2)
	if sum1 > sum2 {
		fmt.Println(sum1, " is Greater")
	} else if sum1 < sum2 {
		fmt.Println(sum2, " is greater")
	}
	// ARRAYS!
	fmt.Println("\nArrays")
	fmt.Println("1. Static Array")
	var array1 [5]int //Static Array !
	fmt.Println(array1)
	array1[3] = 50
	fmt.Println(array1)

	fmt.Println("2. Dynamic Array")
	// Dynamic array
	array2 := []int{5, 6, 7, 8, 9}
	fmt.Println(array2)
	array2 = append(array2, 44)
	array2 = append(array2, 0)
	fmt.Println(array2)

	//---------------------------------------------------
	fmt.Println("\nLoops\nGolang has only For Loops which can be altered to behave like other loops, such as while")

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}
	fmt.Println("Using for as While loop")
	j := 0
	for j < 6 {
		fmt.Println("New j value= ", j)
		j++

	}
	fmt.Println("\n\nMaps\n")

	RollNumber := make(map[string]int)
	RollNumber["Shady"] = 55
	RollNumber["Batman"] = 7
	RollNumber["Superman"] = 69
	fmt.Println(RollNumber)

	delete(RollNumber, "Superman")
	fmt.Println(RollNumber)
}
