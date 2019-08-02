def	ft_bintodec(binary):
	i = 0
	mult = 1

	while (binary != 0):
		i += (binary % 10) * mult
		binary = binary // 10
		mult *= 2
	return (i)
