package main

import (
	"fmt"
	"math/rand"
	"time"
)


func getRandomNum() int {
	rand.Seed(time.Now().UnixNano())
	return rand.Intn(100-0)
}

func main() {
	quit := 0
	pcNum := getRandomNum()
	var ptr *int = &quit
	var userTries int = 3
	var ptrTries *int = &userTries

	fmt.Println("You have 3 chances to guess my number,\nan integer between 0 and 100 (inclusive).\nGood luck!")

	for {
		if quit == 0 {
			playGame(ptr, ptrTries, pcNum)
		} else {
			break
		}
	}
}

func playGame(ptr *int, ptrTries *int, pcNum int) {
	var userGuess int

	if *ptrTries > 0 {
		fmt.Print("Guess my number: ")
		fmt.Scanf("%d", &userGuess)

		if userGuess == pcNum {
			fmt.Println("You win!")
			*ptr = 1
		} else if userGuess > pcNum {
			fmt.Println("My number is smaller!")
			*ptrTries -= 1
		} else {
			fmt.Println("My number is bigger!")
			*ptrTries -= 1
		}
	} else {
		fmt.Println("Game over.\nMy number was ", pcNum)
		*ptr = 1
	}
}
