#include <stdio.h>

//		with getchar() and putchar() you can write a 
//		surprising amount of useful code without
//		knowing anything more about input and output.:w

int main(void)
{	

	int	c ;
	while ( (c = getchar()) != EOF ) // EOF is an integer defined in <stdio.h>
	{
		putchar(c);
	}

	return 0;
}
