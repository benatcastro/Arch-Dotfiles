# include <stdio.h>
# include <stdlib.h>
# include <sys/types.h>
# include <unistd.h>
# include <signal.h>

void signal_handler(int signum, siginfo_t *siginfo, void *ucontext)
{
	if (signum != SIGUSR1) return;
	if (siginfo->si_code != SI_QUEUE) return;

	printf("receiver: Got value %d STRING: %s\n", siginfo->si_int, siginfo->si_ptr);
}

int main(int argc, char **argv
{
	pid_t pid = getpid();
	struct sigaction s_action;

	s_action.sa_sigaction = signal_handler;
	sigemptyset (&s_action.sa_mask);
	s_action.sa_flags = SA_SIGINFO;
	sigaction(SIGUSR1, &s_action, NULL);

	while(1)
		sleep(100);
	return EXIT_SUCCESS;
}
