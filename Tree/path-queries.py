# Euler tour from Senior video in youtibe

import math
from collections import defaultdict

n, q = map(int, input().split())
a = [int(x) for x in input().split()]
arr = [[int(x) for x in input().split()] for _ in range(n-1)]
queries = [[int(x) for x in input().split()] for _ in range(q)]

time = 0
adj = defaultdict(list)

start = [0] * (n+1)
end = [0] * (n+1)

# with open('test_input.txt', 'r') as file:
#     n, q = map(int, file.readline().split())
#     arr = [int(x) for x in file.readline().split()]
#     queries = [[int(x) for x in file.readline().split()] for _ in range(q)]

x = math.ceil(math.log2(2*(n+1)))

# Seg tree max size
max_size = 2 * (2 ** x) - 1

segmentTree = [0] * (max_size)

def constructSegTree(low, high, pos):
    if low == high:
        segmentTree[pos] = arr[low]
        return
    mid = (low+high) // 2
    constructSegTree(low, mid, 2*pos + 1)
    constructSegTree(mid+1, high, 2*pos + 2)
    segmentTree[pos] = segmentTree[2*pos+1] + segmentTree[2*pos+2]

def updateSegTree(index, val, low, high, pos):
    if index<low or index>high:
        return
    if low == high:
        segmentTree[pos] = val
        return
    mid = (low+high) // 2
    updateSegTree(index, val, low, mid, 2*pos+1)
    updateSegTree(index, val, mid+1, high, 2*pos+2)
    segmentTree[pos] = segmentTree[2*pos+1] + segmentTree[2*pos+2]

def findRangeSum(qLow, qHigh, low, high, pos):
    if qLow<=low and qHigh>=high:
        return segmentTree[pos]
    if qLow>high or qHigh<low:
        return 0
    mid = (low+high) // 2
    return findRangeSum(qLow, qHigh, low, mid, 2 * pos+1) + findRangeSum(qLow, qHigh, mid+1, high, 2 * pos+2)

def dfs(node, par):
    global time
    start[node] = time
    time += 1
    for it in adj[node]:
        if it != par:
            dfs(it, node)
    
    end[node] = time
    time += 1
    
# constructSegTree(0, n-1, 0)
for e1, e2 in arr:
    adj[e1].append(e2)
    adj[e2].append(e1)

dfs(1, 0)

for i in range(1, n+1):
    updateSegTree(start[i], a[i-1], 0, 2*n-1, 0)

for i in range(1, n+1):
    updateSegTree(end[i], -a[i-1], 0, 2*n-1, 0)

for i in range(len(queries)):
    q1 = queries[i][0]
    q2 = queries[i][1]
    if q1 == 1:
        q3 = queries[i][2]
        updateSegTree(start[q2], q3, 0, 2*n-1, 0)
        updateSegTree(end[q2], -q3, 0, 2*n-1, 0)
    else:
        print(findRangeSum(start[1], end[q2]-1, 0, 2*n-1, 0))


