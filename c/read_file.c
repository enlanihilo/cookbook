#include <stdio.h>
#include <stdlib.h>

#define MAXCHAR 1000

int main(void)
{
	const char *filename = "test.txt";
	FILE *fp = NULL;
	char str[MAXCHAR];
	
	//open file
	fp = fopen(filename, "r");

	if (fp == NULL)
	{
		printf("Error opening %s\n", filename);
		exit(1);
	}

	while (fgets(str, MAXCHAR, fp) != NULL)
	{
		printf("%s", str);
	}

	fclose(fp);
	return 0;
}
