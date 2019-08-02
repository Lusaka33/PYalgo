def	ft_power(nbr, power):
	if (power < 0):
		return (0)
	elif (power > 0):
		return (nbr * ft_power(nbr, power - 1))
	else:
		return (1)

