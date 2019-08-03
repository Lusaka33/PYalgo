def	ft_selectsort(arr):
	i = 0

	while (i < (len(arr) - 1)):
		j = i
		while (j <= (len(arr) - 1)):
			if (arr[j] < arr[i]):
				arr[i], arr[j] = arr[j], arr[i]
			j += 1
		i += 1
	return (arr)
