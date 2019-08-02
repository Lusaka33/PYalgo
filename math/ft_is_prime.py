def ft_is_prime(nbr):
	i = 2

	if (nbr < 2):
		return (0)
	elif (nbr == 2):
		return (2)
	while (((nbr % i) != 0) and i < nbr):
		i += 1
		if (i == nbr):
			return (i)
	return (0)
