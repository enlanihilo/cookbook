#include <stdio.h>

/*
	The zeroth argument is always the name of the executing binary,
	and the rest of the argument array (often called argument vector [argv])
	contains the remaining arguments as strings.
*/


int main(int arg_count, char *arg_list[])
{
	int i;
	printf("There were %d arguments provided:\n", arg_count);

	for (i=0; i<arg_count; ++i)
		printf("argument #%d\t-\t%s\n", i, arg_list[i]);

	return 0;
}
