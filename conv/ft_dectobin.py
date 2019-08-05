def	ft_dectobin(decimal):
	if (decimal < 0):
		return ('Not a positive number')
	elif (decimal == 0):
		return (0)
	else:
		return ((decimal % 2) + (10 * ft_dectobin(decimal // 2)))
