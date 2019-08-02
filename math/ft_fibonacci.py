def	ft_fibonacci(index):
	if (index < 0):
		return (-1)
	elif (index == 0):
		return (0)
	elif (index == 1):
		return (1)
	return (ft_fibonacci(index - 1) + ft_fibonacci(index -2))
