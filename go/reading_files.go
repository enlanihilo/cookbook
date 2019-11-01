package main

import (
	"fmt"
	"os"
)

//run the writing_files.go program first to create
//the test.txt file

func main () {
	
	file, err := os.Open("test.txt")  
	if err != nil {
		fmt.Println(err)
	}

	//data read into slice of bytes
	data := make([]byte, 100)
	count, err := file.Read(data)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Printf("read %d bytes: %q\n", count, data[:count])

}
