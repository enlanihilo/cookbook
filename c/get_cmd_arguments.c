#include <stdio.h>

int main(int args, char *argv[]) {
 	int i = 0;
	for (i; i < args; i++)
		printf("\n%s", argv[i]);
	return 0;
}
