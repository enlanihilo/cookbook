import socket

#docs/guide : docs.python.org/3.7/howto/sockets.html

#create INET (IPv4), STREAM (TCP) socket 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket to a public host, and well-known port
serversocket.bind((socket.gethostname(), 1237))

# become a server socket
serversocket.listen(5)

while True:
    #accept connections from outside
    (clientsocket, address) = serversocket.accept()

    #now do something with the clientsocket
    print(f"connection from {address} established!")
    clientsocket.send(bytes("Welcome to the server", "utf-8"))

