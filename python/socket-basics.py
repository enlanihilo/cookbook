import socket

"""
    socket = interface between Application Layer <--> Transportation Layer

    The socket module provides access to the BSD socket interface, available on all modern
    Unix systems, windows, macos and additional platforms.

    PS: some behavior may be platform dependent since calls are made to the OS socket API.

"""

#create INET (IPv4), SREAM (TCP) socket                     # Roughly speaking, when you visit
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # a link, that's what a browser
                                                            # does.
#bing socket to a public host + port                        # When connect completes, the socket
s.connect(("www.python.org", 80))                           # s can be used to send in a request

