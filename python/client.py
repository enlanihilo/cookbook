import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1237))

while True:
#            buffer size
    msg = s.recv(8)
    print(msg.decode("utf-8"))