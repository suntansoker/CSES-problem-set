from bisect import bisect_left
n = int(input())
arr = [int(y) for y in input().split()]

res = []
count = 0

for i in range(len(arr)):
    if len(res) == 0:
        res.append(arr[i])
        count += 1
    else:
        pos = bisect_left(res, arr[i])
        if pos==len(res):
            res.append(arr[i])
            count += 1
        else:
            res[pos] = arr[i]

print(count)