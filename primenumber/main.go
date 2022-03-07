package main
//check prime numbers
//number only divisible by itself or 1

import (
	"fmt"
	"math"
)

func checkprime(num int){
	if num < 2 {
		fmt.Println("number must be greater than 2")
	    return
	}

	sqroot := int(math.Sqrt(float64(num)))
	for i:=2; i<=sqroot; i++ {
		if num % i == 0 {
			fmt.Println("is Non prime number")
			return
		} 
	}

	fmt.Println( "is prime number")
	return
}

func main(){
	checkprime(3)
}