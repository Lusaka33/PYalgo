def	ft_arrswap(arr, b, c):
	arr[b], arr[c] = arr[c], arr[b]

def ft_partition(arr, start, end):
	temp = start
	temp2 = temp
	while (temp < end):
		if (arr[temp] <= arr[end]):
			ft_arrswap(arr, temp2, temp)
			temp2 += 1
		temp += 1
	ft_arrswap(arr, temp2, end)
	return (temp2)

def	ft_quicksort(arr, start = 0, end = None):
	if (end == None):
		end = len(arr) - 1
	if (start >= end):
		return (0)
	p = ft_partition(arr, start, end)
	ft_quicksort(arr, start, p - 1)
	ft_quicksort(arr, p + 1, end)
