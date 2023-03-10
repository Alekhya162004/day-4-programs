def minJumps(arr, l, h):
	if (h == l):
		return 0
	if (arr[l] == 0):
		return float('inf')
	min = float('inf')
	for i in range(l + 1, h + 1):
		if (i < l + arr[l] + 1):
			jumps = minJumps(arr, i, h)
			if (jumps != float('inf') and
					jumps + 1 < min):
				min = jumps + 1
	return min
array=list(map(int,input("Enter an array of numbers: ").split(',')))     
print(array)
n = len(array)
print('Minimum number of jumps to reach end is', minJumps(array, 0, n-1))
Footer
