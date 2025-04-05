# Idea: arr[i] + |j- i| implies arr[i] + i - j if i>=j or arr[i] - i + j if i<=j
# It means for each i, we construct 2 seg tree, uptree = arr[i] + i and downtree = arr[i] - i
# After that for each query index j, we find min in downtree[0...j] and min in uptree[j...n-1]
# After that, we find min between min(downtree[0..j]) + j and min(uptree[j...n-1]) - j

n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

class SegmentTree:
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.tree = [10 ** 15] * (4 * self.n)

    def merge(self, val1, val2):
        return min(val1, val2)

    def build(self, pos, low, high):
        if low == high:
            self.tree[pos] = self.arr[low]
            return
        mid = (low + high) // 2
        self.build(2 * pos + 1, low, mid)
        self.build(2 * pos + 2, mid + 1, high)
        self.tree[pos] = self.merge(self.tree[2 * pos + 1], self.tree[2 * pos + 2])

    def update(self, pos, low, high, index, val):
        if index<low or index>high:
            return
        if low == high:
            self.tree[pos] = val
            return
        mid = (low + high) // 2
        self.update(2 * pos + 1, low, mid, index, val)
        self.update(2 * pos + 2, mid + 1, high, index, val)
        self.tree[pos] = self.merge(self.tree[2 * pos + 1], self.tree[2 * pos + 2])

    def query(self, pos, qLow, qHigh, low, high):
        if qHigh<low or qLow>high:
            return 10 ** 15
        if qLow<=low and high<=qHigh:
            return self.tree[pos]
        mid = (low + high) // 2
        return self.merge(self.query(2*pos+1, qLow, qHigh, low, mid), self.query(2*pos+2, qLow, qHigh, mid+1, high))

upArr = [(arr[i] + i) for i in range(n)]
downArr = [(arr[i] - i) for i in range(n)]

upTree = SegmentTree(upArr, n)
downTree = SegmentTree(downArr, n)

upTree.build(0, 0, n-1)
downTree.build(0, 0, n-1)

for i in range(q):
    bIndex = queries[i][1] - 1  #building index 
    if queries[i][0] == 1:
        newPrice = queries[i][2] #new pizza prize
        upTree.update(0, 0, n-1, bIndex, newPrice+bIndex)
        downTree.update(0, 0, n-1, bIndex, newPrice-bIndex)
    else:
        upMin = upTree.query(0, bIndex, n - 1, 0, n-1) - bIndex
        downMin = downTree.query(0, 0, bIndex, 0, n-1) + bIndex
        print(min(upMin, downMin))








