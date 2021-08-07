arr = [int(num) for num in input().split()]

idx1 = int(input()) - 1
idx2 = int(input()) - 1

# swap thang tren python
arr[idx1], arr[idx2] = arr[idx2], arr[idx1]

# swap k can bien phu
# arr[idx1] += arr[idx2]
# arr[idx2] = arr[idx1] - arr[idx2]
# arr[idx1] = arr[idx1] - arr[idx2]

# swap su dung bien phu
# temp = arr[idx1]
# arr[idx1] = arr[idx2]
# arr[idx2] = temp

print(*arr, sep=', ')

# a = a + b
# b = a - b
# a = a - b

# a = tmp
# a = b
# b = tmp
