import math

n, q = map(int, input().split())
arr = [int(x) for x in input().split()]
queries = [[int(x) for x in input().split()] for _ in range(q)]

# with open('test_input.txt', 'r') as file:
#     n, q = map(int, file.readline().split())
#     arr = [int(x) for x in file.readline().split()]
#     queries = [[int(x) for x in file.readline().split()] for _ in range(q)]

x = math.ceil(math.log2(n))

# Seg tree max size
max_size = 2 * (2 ** x) - 1

MAX = 10 ** 18

segmentTree = [MAX] * (max_size)

def constructSegTree(low, high, pos):
    if low == high:
        segmentTree[pos] = arr[low]
        return
    mid = (low+high) // 2
    constructSegTree(low, mid, 2*pos + 1)
    constructSegTree(mid+1, high, 2*pos + 2)
    segmentTree[pos] = min(segmentTree[2*pos+1], segmentTree[2*pos+2])

def findRangeMin(qLow, qHigh, low, high, pos):
    if qLow<=low and qHigh>=high:
        return segmentTree[pos]
    if qLow>high or qHigh<low:
        return MAX
    mid = (low+high) // 2
    return min(findRangeMin(qLow, qHigh, low, mid, 2 * pos+1), findRangeMin(qLow, qHigh, mid+1, high, 2 * pos+2))

constructSegTree(0, n-1, 0)

for q1, q2 in queries:
    print(findRangeMin(q1-1, q2-1, 0, n-1, 0))


