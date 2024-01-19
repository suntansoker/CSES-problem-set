from sortedcontainers import SortedSet

from bisect import bisect_left

n = int(input())
arr = [list(int(y) for y in input().split())+[i] for i in range(n)]

res_contains = [0] * n
res_contained = [0] * n

# Sort first on  the left index asc and then on the right index dsc
# Example:
# 1, 6
# 2, 4
# 3, 6
# 4, 8

newArr = sorted(arr, key = lambda x: (x[0], -x[1]))

st1 = SortedSet()
st2 = SortedSet()
# st1 = set()
# st2 = set()
for index, a in enumerate(newArr):
    # idx = bisect_left(sorted(st1), (a[1], -index))
    idx = bisect_left(st1, (a[1], -index))
    st1.add((a[1], -index))
    res_contained[a[2]] = len(st1) - 1 - idx

for index, a in reversed(list(enumerate(newArr))):
    # idx = bisect_left(sorted(st2), (a[1], -index))
    idx = bisect_left(st2, (a[1], -index))
    st2.add((a[1], -index))
    res_contains[a[2]] = idx

print(' '.join([str(x) for x in res_contains]))
print(' '.join([str(x) for x in res_contained]))