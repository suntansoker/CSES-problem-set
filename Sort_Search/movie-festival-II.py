# NEED TO UNDERSTAND

from bisect import bisect_right

from sortedcontainers import SortedList

n, k = map(int, input().split())
arr = [list(int(y) for y in input().split()) + [i] for i in range(n)]


cnt = 0

arr.sort(key=lambda x: x[1])

# WITHOUT USING SORTEDLIST

# pq = []

# for a in arr:
#     if len(pq) == 0:
#         pq.append((-a[1], a[2]))
#         pq.sort()
#     else:
#         pos = bisect_right(pq, (-a[0], -1))
#         if pos != len(pq):
#             pq.pop(pos)
#             pq.append((-a[1], a[2]))
#             pq.sort()
#         elif pos == len(pq) and len(pq) < k:
#             pq.append((-a[1], a[2]))
#             pq.sort()
#         else:
#             cnt += 1

# print(n - cnt)

# USING SORTEDLIST

pq = SortedList()

for a in arr:
    if len(pq) == 0:
        pq.add((-a[1], a[2]))
    else:
        pos = bisect_right(pq, (-a[0], -1))
        if pos != len(pq):
            pq.pop(pos)
            pq.add((-a[1], a[2]))
        elif pos == len(pq) and len(pq) < k:
            pq.add((-a[1], a[2]))
        else:
            cnt += 1

print(n - cnt)

    