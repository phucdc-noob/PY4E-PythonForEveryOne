arr = [int(num) for num  in input().split()]

sArr = [] #sorted array

for i in range(len(arr)):
    sArr.append(min(arr))
    arr.remove(min(arr))
print(*sArr, sep="\n")