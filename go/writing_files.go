package main

import (
	"fmt"
	"os"
)


func main () {
	testTxt, err := os.Create("test.txt")
	if err != nil {
		fmt.Println(err)
		return
	}

	l, err := testTxt.WriteString("Hello go!\n")
	if err != nil {
		fmt.Println(err)
		testTxt.Close()
		return
	}

	fmt.Println(l, "Bytes written successfully!")
	err = testTxt.Close()
	if err != nil {
		fmt.Println(err)
		return
	}
}

