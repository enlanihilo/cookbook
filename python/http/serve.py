#!/usr/bin/python3

import os
import sys
import socket

if len(sys.argv) <= 1:
    PORT = 80
else:
    PORT = int(sys.argv[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', PORT))
sock.listen(2)

def full_path(path):
    return os.path.join( os.getcwd(), path.strip('/') )


def send(conn, path):
    with open(full_path(path)) as file:
        content = file.read()
        conn.send(str.encode(content))

def error(conn):
    send(conn, 'error.html')    
    conn.close()

while True:
    (conn, addr) = sock.accept()

    data = conn.recv(1024)
    tokens = data.split(str.encode(' '))
    
    if len(tokens) < 2:
        error(conn)
        continue

    print(f'Server got: {data}')
    print(f'path: {tokens[1]}')

    path = tokens[1]

    if path in ['/', '/index.html']:
        send(conn, 'index.html')
    elif os.path.exists(full_path(path)):
        send(conn, full_path(path))
    else:
        error(conn)
        continue
            
    conn.close()

