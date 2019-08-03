def	ft_insertsort(arr):
	i = 1

	while (i < len(arr)):
		k = arr[i]
		j = i - 1
		while (j >= 0 and arr[j] > k):
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = k
		i += 1
	return (arr)
