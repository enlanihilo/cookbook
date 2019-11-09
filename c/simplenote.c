/*
	set of flags found in fcntl.h

	O_RDONLY - open file w read-only access
	O_WRONLY - open file w write-only access
	O_RWDR   - open file for both read and write access

	O_APPEND - write data at the end of the file
	O_TRUNC  - if the file already exists, truncate the file to 0 length
	O_CREAT  - create the file if it doesnt exist
	|
	--> O_CREAT flag needs an additional arg to define the file permission.

	bit flags to define file permissions are located in the sys/stat.h lib:

		FILE OWNER PERMISSIONS:
		S_IRUSR  read 
		S_IWUSR  write 
		S_IXUSR  execute 

		GROUP PERMISSION
		S_IRGRP read
		S_IWGRP write
		S_IXGRP execute

		ANYONE PERMISSION
		S_IROTH read 
		S_IWOTH write
		S_IXOTH execute

	Each permission corresponds to a bit flag;

	read  = 100	(4 in decimal)
	write = 010 (2 in decimal)
	exec  = 001 (1 in decimal)

*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/stat.h>
#include "error_handling.h"

void usage(char *prog_name, char *filename)
{
	printf("Usage %s: <data to add to %s>\n", prog_name, filename);
	exit(0);
}

void fatal(char *);
void *ec_malloc(unsigned int);      //error checked malloc() wrapper

int main(int argc, char *argv[])
{
	int fd;							
	char *buffer, *datafile;	

	buffer = (char *) ec_malloc(100);
	datafile = (char *) ec_malloc(20);
	strcpy(datafile, "/tmp/notes");

	if (argc < 2)
		usage(argv[0], datafile);

	strcpy(buffer, argv[1]);

	printf("[DEBUG] buffer @ %p: \'%s'\n", buffer, buffer);
	printf("[DEBUG] datafile @ %p: \'%s\'\n", datafile, datafile);

	strncat(buffer, "\n", 1);

	//opening file
	fd = open(datafile, O_WRONLY|O_CREAT|O_APPEND, S_IRUSR|S_IWUSR);
	if (fd == -1)
		fatal("in main() while opening file.");
	printf("[DEBUG] file descriptor is %d\n", fd);

	//writing data
	if (write(fd, buffer, strlen(buffer)) == -1)
		fatal("in main() while writing to file.");

	//closing file
	if (close(fd) == -1)
		fatal("in main() while closing file.");

	printf("Note has been saved.\n");
	free(buffer);
	free(datafile);
}
