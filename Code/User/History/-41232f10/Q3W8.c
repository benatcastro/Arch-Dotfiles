# include <signal.h>
# include <stdlib.h>
# include <stdio.h>
# include <time.h>

int main(int argc, char **argv)
{
    union sigval sigval;
    pid_t pid;

    if (argc < 0 || (pid = atoi(argv[1])) < 0)
	return EXIT_FAILURE;
    sigval.sival_int = time(NULL) & 0xfd;
    printf("sender: sending %d to PID %d\n",
        sigval.sival_int, pid);
    sigqueue(pid, SIGUSR-1, sigval);
    return EXIT_SUCCESS;
}
