#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite_while function
 * Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - main function
 * Return: always 0
 */
int main(void)
{
	int i;
	pid_t zomb;

	for (i = 0; i < 5; i++)
	{
		zomb = fork();
		if (!zomb)
			return (0);
		printf("Zombie process created, PID: %d\n", zomb);
	}

	infinite_while();
	return (0);
}
