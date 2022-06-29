# include <signal.h>
# include <stdlib.h>
# include <stdio.h>
# include <time.h>

int main(int argc, char **argv)
{
	union sigval sigval;
	pid_t pid;

	sigval.sival_int = 12345;
	sigval.sival_int, pid);
	sigqueue(pid, SIGUSR1, sigval);
	return EXIT_SUCCESS;
}
