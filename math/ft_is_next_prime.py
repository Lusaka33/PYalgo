def	ft_is_next_prime(nbr):
	while (nbr > 2):
		i = 2
		while (i <= nbr):
			if not (nbr % i):
				if (nbr == i):
					return (i)
				break
			i += 1
		nbr += 1
	return (2)
