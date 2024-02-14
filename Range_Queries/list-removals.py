import math

n = int(input())
arr = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]

# with open('test_input.txt', 'r') as file:
#     n = int(file.readline())
#     arr = [int(x) for x in file.readline().split()]
#     queries = [int(x) for x in file.readline().split()]

x = math.ceil(math.log2(n))

# Seg tree max size
max_size = 2 * (2 ** x) - 1

segmentTree = [0] * (max_size)

def constructSegTree(low, high, pos):
    if low == high:
        segmentTree[pos] += 1
        return
    mid = (low + high) // 2
    constructSegTree(low, mid, 2 * pos+1)
    constructSegTree(mid+1, high, 2 * pos + 2)
    segmentTree[pos] = segmentTree[2*pos+1] + segmentTree[2*pos+2]

def update(val, low, high, pos):
    if low == high:
        segmentTree[pos] -= 1
        print(arr[low], end=" ")
        return
    mid = (low + high) // 2
    if segmentTree[2 * pos +1]>=val:
        update(val, low, mid, 2 * pos + 1)
    else:
        update(val - segmentTree[2 * pos +1], mid+1, high, 2 * pos+2)
    segmentTree[pos] = segmentTree[2*pos+1] + segmentTree[2*pos+2]

constructSegTree(0, n-1, 0)

for q in queries:
    update(q, 0, n-1, 0)