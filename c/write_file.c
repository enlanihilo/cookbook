#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct person 
{
	int id;
	char fname[20];
	char lname[20];
};

int main(void)
{
	FILE *outfile;

	//open file
	outfile = fopen("person.dat", "w");

	if (outfile == NULL)
	{
		fprintf(stderr, "\nError opening file\n");
		exit (1);
	}

	struct person input1 = {1, "rohan", "sharma"};
	struct person input2 = {2, "mahendra", "dhoni"};

	fwrite(&input1, sizeof(struct person), 1, outfile);
	fwrite(&input2, sizeof(struct person), 1, outfile);

	if (fwrite != 0)
		printf("contents to file written.\n");
	else
		printf("error writing file!\n");

	//close file
	fclose(outfile);

	return 0;
}

