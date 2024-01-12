from bisect import bisect_right

n = int(input())
arr = [int(y) for y in input().split()]

a = []
l = 0

for i in range(len(arr)):
    pos = bisect_right(a, arr[i])
    if pos >= l:
        l += 1
        a.append(arr[i])
    else:
        a[pos] = arr[i]

print(l)
