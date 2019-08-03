def	ft_bubblesort(arr):
	i = 0
	while (i < (len(arr) - 1)):
		j = 0
		while (j < ((len(arr) - i) - 1)):
			if (arr[j] > arr[j + 1]):
				temp = arr[j]
				arr[j] = arr[j + 1]
				arr[j + 1] = temp
			j += 1
		i += 1
	return (arr)
