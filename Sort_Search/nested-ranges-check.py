n = int(input())
arr = [list(int(y) for y in input().split())+[i] for i in range(n)]


# Sort first on  the left index asc and then on the right index dsc
# Example:
# [2, 6]
# [2, 5]
# ...

newArr = sorted(arr, key = lambda x: (x[0], -x[1]))

res_contains = [0] * n
res_contained = [0] * n

max_right = 0
for i in range(n):
    idx = newArr[i][2]
    if newArr[i][1] <= max_right:
        res_contained[idx] = 1
    else:
        max_right = newArr[i][1]
        res_contained[idx] = 0

min_right = 10 ** 12
for i in range(n-1, -1, -1):
    idx = newArr[i][2]
    if newArr[i][1] >= min_right:
        res_contains[idx] = 1
    else:
        min_right = newArr[i][1]
        res_contains[idx] = 0

print(' '.join([str(x) for x in res_contains]))
print(' '.join([str(x) for x in res_contained]))


