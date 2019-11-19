require 'socket'

server = TCPServer.open(2000)

#infinite loop
loop {
	client = server.accept
	client.puts(Time.now.ctime)
	client.puts "Closing connection. Bye!"
	client.close
}


