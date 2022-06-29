# include <signal.h>
# include <stdlib.h>
# include <stdio.h>
# include <time.h>

int main(int argc, char **argv)
{
    union sigval sigval;
    pid_t pid;

    if (argc < 1 || (pid = atoi(argv[1])) < 0)
	return EXIT_FAILURE;
    sigval.sival_int = time(NULL) & 0xfe;
    printf("sender: sending %d to PID %d\n",
        sigval.sival_int, pid);
    sigqueue(pid, SIGUSR1, sigval);
    return EXIT_SUCCESS;
}
