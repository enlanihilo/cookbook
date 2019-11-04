/*
  Code Author: Jacob Sorber
  Check out his youtube channel. great C content!
  I typed this code from his video:
  	https://www.youtube.com/watch?v=bdIiTxtMaKA

  This program acts as a "web browser", with no GUI ofc :p
  Usage: 
		./TCP_socket <ip.address>
*/

#include <stdio.h>
#include <fcntl.h>
#include <netdb.h>
#include <errno.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <unistd.h>
#include <stdarg.h>
#include <sys/time.h>
#include <sys/ioctl.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>

#define SERVER_PORT 80

//buffer length (where data goes)
#define MAXLINE 4096
#define SA struct sockaddr

//error handling
void err_n_die(const char *fmt, ...);

int main(int argc, char **argv)
{
	int sockfd, n;
	int sendbytes;
	char sendline[MAXLINE];
	char recvline[MAXLINE];
	struct sockaddr_in servaddr;

	//usage check 2:16
	if (argc != 2)
		err_n_die("usage: %s <server address>", argv[0]);

	//create a new socket 2:31
	if ( (sockfd = socket(AF_INET, SOCK_STREAM, 0)) < 0)
		err_n_die("Error while creating the socket!");

	//
	bzero(&servaddr, sizeof(servaddr));
	servaddr.sin_family = AF_INET;
	servaddr.sin_port = htons(SERVER_PORT);

	//convert string rappresentation of addres to binary
	if (inet_pton(AF_INET, argv[1], &servaddr.sin_addr) <= 0)
		err_n_die("inet_pton error for %s ", argv[1]);

	//connect to the server
	if (connect(sockfd, (SA *) &servaddr, sizeof(servaddr)) < 0)
		err_n_die("connect failed.");

	//connection established. Prepare the msg
	sprintf(sendline, "GET / HTTP/1.1\r\n\r\n");
	sendbytes = strlen(sendline);

	//send request 5:00
	if (write(sockfd, sendline, sendbytes) != sendbytes)
		err_n_die("write error");
	
	memset(recvline, 0, MAXLINE);

	//now read server's response
	while ( (n = read(sockfd, recvline, MAXLINE-1)) > 0)
	{
		printf("%s", recvline);
	}
	if (n < 0)
		err_n_die("read error");

	//end successfully.
	exit(0);
}

//2:03
void err_n_die(const char *fmt, ...)
{
	int errno_save;
	va_list ap;
	errno_save = errno;

	va_start(ap, fmt);
	vfprintf(stdout, fmt, ap);
	fprintf(stdout, "\n");
	fflush(stdout);

	if (errno_save != 0)
	{
		fprintf(stdout, "(errno = %d) : %s\n", errno_save, strerror(errno_save));
		fprintf(stdout, "\n");
		fflush(stdout);
	}
	va_end(ap);

	//the die part... terminates program with an error.
	exit(1);
}

