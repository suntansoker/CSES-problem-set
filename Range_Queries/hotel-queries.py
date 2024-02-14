import math

n, q = map(int, input().split())
arr = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]

x = math.ceil(math.log2(n))
max_size = 2 * (2 ** x) - 1

MIN = - (10 ** 18)
segmentTree = [MIN] * max_size

def buildSegTree(low, high, pos):
    if low == high:
        segmentTree[pos] = arr[low]
        return
    mid = (low + high) // 2
    buildSegTree(low, mid, 2 * pos + 1)
    buildSegTree(mid + 1, high, 2 * pos + 2)
    segmentTree[pos] = max(segmentTree[2 * pos + 1], segmentTree[2 * pos + 2])

def updateSegTree(low, high, val, pos):
    if low==high:
        segmentTree[pos] -= val
        print(low+1, end=" ")
        return
    mid = (low + high) // 2
    if segmentTree[2 * pos + 1]>= val:
        updateSegTree(low, mid, val, 2 * pos + 1)
    else:
        updateSegTree(mid+1, high, val, 2 * pos + 2)
    segmentTree[pos] = max(segmentTree[2 * pos + 1], segmentTree[2 * pos + 2])

buildSegTree(0, n-1, 0)

for q in queries:
    if segmentTree[0]<q:
        print(0, end=' ')
    else:
        updateSegTree(0, n-1, q, 0)