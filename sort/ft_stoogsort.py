def	ft_arrswap(arr, b, c):
	arr[b], arr[c] = arr[c], arr[b]

def	ft_stoogesort(arr, i = 0, j = None):
	if (j is None):
		j = len(arr) - 1
	if (arr[i] > arr[j]):
		ft_arrswap(arr, i, j)
	if (j - i > 1):
		temp = (j - i + 1) // 3
		ft_stoogesort(arr, i, j - temp)
		ft_stoogesort(arr, i + temp, j)
		ft_stoogesort(arr, i, j - temp)
	return (arr)
