def count_split(arr, temp_arr, left, mid, right):
	i = left
	j = mid + 1
	k = left
	inv_cnt = 0

	while i <= mid and j <= right:
		if arr[i] <= arr[j]:
			temp_arr[k] = arr[i]
			k += 1
			i += 1
		else:
			temp_arr[k] = arr[j]
			inv_cnt += (mid-i + 1)
			k += 1
			j += 1

	while i <= mid:
		temp_arr[k] = arr[i]
		k += 1
		i += 1

	while j <= right:
		temp_arr[k] = arr[j]
		k += 1
		j += 1

	for idx in range(left, right + 1):
		arr[idx] = temp_arr[idx]
		
	return inv_cnt

def count(arr, temp_arr, left, right):
	inv_cnt = 0

	if left < right:
		mid = (left + right)//2
		inv_cnt += count(arr, temp_arr, left, mid)
		inv_cnt += count(arr, temp_arr, mid + 1, right)
		inv_cnt += count_split(arr, temp_arr, left, mid, right)
  
	return inv_cnt


while True:
    n = int(input())
    if not n: break
    
    arr = list(map(int, input().split()))
    
    result = count(arr, [0] * n, 0, n-1)
    print(result)