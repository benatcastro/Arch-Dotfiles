/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bena <bena@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/27 22:43:47 by bena              #+#    #+#             */
/*   Updated: 2022/06/29 01:39:15 by bena             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <signal.h>
#include "ft_printf.h"

int g_index;

void	showbits(unsigned char x )
{
	int	i;

	i = 0;
	for (i = (sizeof(char) * 8) - 1; i >= 0; i--)
	{
		putchar(x & (1u << i) ? '1' : '0');
	}
	printf("\n");
}

void	ft_signal_handler(int signum, siginfo_t *data, void *ucontext)
{
	char			c;
	int				i;
	int				j;


	(void)signum;
	(void)ucontext;


	if (data->si_int == -1)
	{
		//ft_printf("\n");
		//showbits(c);
		ft_printf("%c", c);
		ft_printf("\nFinished");
	}
	else
	{
		if (data->si_int == 1)
			c |= (1 << (7 - g_index));
		else if (data->si_int == 0)
			c |= (0 << (7 - g_index));
		g_index++;
		//ft_printf("%d", data->si_int);
	}
}

int	main(void)
{
	pid_t				server_pid;
	struct sigaction	signal_action;

	server_pid = getpid();
	printf("SERVER PID: %d\n", server_pid);

	signal_action.sa_sigaction = ft_signal_handler;
	sigemptyset (&signal_action.sa_mask);
	signal_action.sa_flags = SA_SIGINFO;
	sigaction(SIGUSR1, &signal_action, NULL);

	while (1)
		sleep(100);
	return (1);
}
