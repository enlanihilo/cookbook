require 'socket'

soc = TCPSocket.new 'localhost', 2000

while line = soc.gets # listen
	puts line		  # print requests
end

soc.close			  # close socket
