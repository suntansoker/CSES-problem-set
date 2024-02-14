import math

n, q = map(int, input().split())
arr = [int(x) for x in input().split()]
queries = [[int(x) for x in input().split()] for _ in range(q)]

diff = [0] * (n+1)
diff[0] = arr[0]

for i in range(1, n):
    diff[i] = arr[i] - arr[i-1]

x = math.ceil(math.log2(n))

# Seg tree max size
max_size = 2 * (2 ** x) - 1

segmentTree = [0] * (max_size)

def constructSegTree(low, high, pos):
    if low == high:
        segmentTree[pos] = diff[low]
        return
    mid = (low+high) // 2
    constructSegTree(low, mid, 2*pos + 1)
    constructSegTree(mid+1, high, 2*pos + 2)
    segmentTree[pos] = segmentTree[2*pos+1] + segmentTree[2*pos+2]

def updateSegTree(index, val, low, high, pos):
    if index<low or index>high:
        return
    if low == high:
        segmentTree[pos] += val
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
    
constructSegTree(0, n-1, 0)

for idx, mat in enumerate(queries):
    if mat[0] == 1:
        diff[mat[1]-1] += mat[3]
        updateSegTree(mat[1]-1, mat[3], 0, n-1, 0)
        if mat[2] < n:
            diff[mat[2]] += mat[3]
            updateSegTree(mat[2], -mat[3], 0, n-1, 0)
    else:
        print(findRangeSum(0, mat[1]-1, 0, n-1, 0))
