package main

import (
	"net"
	"io"
	"log"
	"fmt"
)

const (
	HOST = "localhost"
	PORT = "2000"
	TYPE = "tcp"
)

func main () {

	/*
	Listen on TCP port 2000 on all available
	unicast and anycast IP addresses of the
	local system. 
	*/

	l, err := net.Listen(TYPE, HOST + ":" + PORT)
	if err != nil {
		log.Fatal(err)
	}

	defer l.Close()

	for {

		//wait connection
		conn, err := l.Accept()
		if err != nil {
			log.Fatal(err)
		}

		//handle the connection in a new
		//goroutine.

		go func(c net.Conn) {
			//echo all incoming data
			fmt.Println("I'm listening")
			c.Write([]byte("Message received\n"))
			io.Copy(c, c)
			//shut down connection
			c.Close()
		}(conn)
	}
}
