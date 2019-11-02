#include <stdlib.h>
#include <stdio.h>
#include <time.h>

void playgame(int *play, int *lives);
int getRandomNum(void); 

int RANDNUM;

int main(int argc, char *argv[])
{
	int play = 1;
	int lives = 3;
	int *ptr_play = &play;
	int *ptr_lives = &lives;
	//this is required to generate a pseudorandom num
	srand(time(NULL));
	RANDNUM = getRandomNum();


	while (play) 
	{
		if (!lives)
		{
			printf("You lost!\n");
			printf("My number was: %d\n",RANDNUM);
			return 0;
		}
		playgame(ptr_play, ptr_lives);
	}

	return 0;
}

void playgame(int *ptr_play, int *ptr_lives) 
{
	int userGuess;  

	//gen random num
	//ask for user input
	printf("Type in your guess: ");
	scanf("%d", &userGuess);

	//compare nums
	if (userGuess == RANDNUM)
	{
		printf("You win!\n");
		*ptr_play = 0;
	} else {
		
		//player loses 1 life
		*ptr_lives -= 1;
		
		if (*ptr_lives > 0) 
		{
			if (userGuess < RANDNUM)
			{
				printf("My num is bigger!\n");
			} else {
				printf("My num is smaller!\n");
			}
		}
	}
}

int getRandomNum(void) 
{
	int min = 0;
	int max = 101;
	int randNum = (((rand() % max) - min) + min );

	//printf("randNum: %d", randNum);
	return randNum;
}
