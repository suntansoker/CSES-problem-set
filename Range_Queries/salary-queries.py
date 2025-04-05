import math
from sortedcontainers import SortedList
# SortedList need to be written as a separate code to pass in some platforms
from collections import defaultdict
from bisect import bisect_left, bisect_right

n, q = map(int, input().split())
arr = [int(x) for x in input().split()]
sl = SortedList()

queries = [[x for x in input().split()] for _ in range(q)]

mp = defaultdict(int)

for i in range(len(arr)):
    sl.add(arr[i])
    mp[i] = arr[i]

for q1, q2, q3 in queries:
    if q1 == '!':
        idx = int(q2) - 1
        val = int(q3)
        oldVal = mp[idx]
        sl.remove(oldVal)
        sl.add(val)
        mp[idx] = val
    else:
        right = sl.bisect_right(int(q3))
        left = sl.bisect_left(int(q2))
        print(right - left)