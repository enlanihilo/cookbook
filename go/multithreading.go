package main

import (
	"fmt"
	"time"
)


func main() {
	//goroutine is a lightweight thread
	//managed by the go runtime
	
	go say("world")
	say("hello")

}

func say(s string) {
	for i:=0; i < 5; i++ {
		time.Sleep(100 * time.Millisecond)
		fmt.Println(s)
	}
}
