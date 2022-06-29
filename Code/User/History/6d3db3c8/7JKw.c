/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: bena <bena@student.42.fr>                  +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/06/27 22:30:26 by bena              #+#    #+#             */
/*   Updated: 2022/06/28 21:43:43 by bena             ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"
#include "signal.h"

static pid_t ft_check_args(char *pid, int argc, char *argv[])
{
	int	i;

	if (argc == 1)
	{
		ft_printf ("usage ./client.exec [Server-PID] [String to send]\n");
		exit (1);
	}
	else if (argc != 3 || !ft_strlen(argv[2]))
	{
		ft_printf("Please enter the PID of the process and the string to send.\n");
		exit (1);
	}
	i = 0;
	while (pid[i] && (ft_isdigit(pid[i]) != 0 || pid[i] == '-'))
		i++;
	if (i != (int)ft_strlen(pid))
	{
		ft_printf("Wrong PID, try again please.\n");
		exit (1);
	}
	else
		return ((pid_t)ft_atoi(pid));
}

/*sends 0 or 1 till the octet of bytes is complet
-1 send when the octet is fully sended*/
static	void	ft_send_char(pid_t pid, unsigned char c)
{
	union sigval	sv;
	int				i;

	i = 8;
	while (i--)
	{
		c >> i & 1 = sv.sival_int;
		printf("%d", sv.sival_int);
		sigqueue(pid, SIGUSR1, sv);
		usleep(100);
	}
	sv.sival_int = -1;
	sigqueue(pid, SIGUSR1, sv);
	usleep(100);
}

int	main(int argc, char	*argv[])
{
	pid_t			pid;

	pid = ft_check_args(argv[1], argc, argv);
	ft_send_char(pid, argv[2][0]);
	//sv.sival_int = ft_atoi(argv[2]);
	//sigqueue(pid, SIGUSR1, sv);
}
