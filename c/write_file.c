/* https://www.youtube.com/watch?v=r7G085NdegY&list=PLCNJWVn9MJuPtPyljb-hewNfwEGES2oIW&index=17&t=0s

<stdio.h>
	METHODS:		FILE *f : structure
		fopen			for C File I/O you need to
		fwrite			use a file pointer, which 
		fread			will let the program keep
		fprintf			track of the file being
		fscanf			accessed.
		fgetc

3 special file types:
	stdin   --> getc
	stdout	<-- printf
	stderr

file operations
w  - write
r  - read
a  - append
rw - read and write
wb - binary mode
a+
r+
w+
*/

#include <stdio.h>
#include <stdlib.h> 

int main(void)
{
	const char *filename = "test.txt";
	FILE *fp = NULL;

	//create file
	fp = fopen(filename, "w+"); //write only
	
	//error handling
	if (fp == NULL)
	{
		fprintf(stderr, "Can't open testing.txt\n");
		exit(1); 
	}

	//write to file
	fprintf(fp, "Testing...\n");

	//close file
	fclose(fp);		

	return 0;
}
