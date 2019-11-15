/* reference: https://github.com/CyberChimeraUSA/C-Networking/blob/master/C-SendHTTPRequest/src.c
*   
*   Linux Programmer's Manual : man pages (best reference)
*       ~$ man recv        - receive message from socket
*       ~$ man getaddrinfo - network address service translation
*       ~$ man socket      - create endpoint for communication 
*/

#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <netdb.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    int rv;
    int sockfd;
    unsigned char buffer[4096];
    struct addrinfo hints, *results;
    
    if (argc != 2)
    {
        fprintf(stderr, "Usage: %s www.<domain>.com", argv[0]);
        exit(1);
    }

    char *inputVal = argv[1];

    memset(&hints, 0, sizeof hints);
    hints.ai_family = AF_UNSPEC;
    hints.ai_socktype = SOCK_STREAM;

    if ( (rv = getaddrinfo( inputVal , "80" , &hints , &results)) != 0)
    {
        fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
        return 1;
    }

    sockfd = socket(results->ai_family, results->ai_socktype, results->ai_protocol);
    connect(sockfd, results->ai_addr, results->ai_addrlen);

    send(sockfd, "HEAD / HTTP/1.0\r\n\r\n", 23, 0);
    int recv_length = 1;
    recv_length = recv(sockfd, &buffer, 1024, 0);
        
    while(recv_length > 0) 
    {
        printf("The web server is %s\n", buffer+8);
        freeaddrinfo(results);
        return 0;
    }

    printf("Server line not found\n");

    freeaddrinfo(results);
    return 0;

}
