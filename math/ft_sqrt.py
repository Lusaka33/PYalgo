def	ft_sqrt(nbr):
	sqrt = 1

	if (nbr < 0):
		return (0)
	while ((sqrt * sqrt) < nbr):
		sqrt += 1
	if ((sqrt * sqrt) == nbr):
		return (sqrt)
	return (0)
