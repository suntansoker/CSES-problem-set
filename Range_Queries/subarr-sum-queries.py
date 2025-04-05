n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

class Node:
    def __init__(self, mSum, lSum, rSum, totalSum):
        self.mSum = mSum 
        self.lSum = lSum 
        self.rSum = rSum 
        self.totalSum = totalSum

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [None] * (4 * self.n)

    def merge(self, leftNode, rightNode):
        newNode = Node(0, 0, 0, 0)
        newNode.mSum = max(leftNode.mSum, rightNode.mSum, leftNode.rSum + rightNode.lSum)
        newNode.lSum = max(leftNode.lSum, leftNode.totalSum + rightNode.lSum)
        newNode.rSum = max(rightNode.rSum, rightNode.totalSum + leftNode.rSum)
        newNode.totalSum = leftNode.totalSum + rightNode.totalSum
        return newNode

    def build(self, pos, low, high):
        if low == high:
            val = max(arr[low], 0)
            self.tree[pos] = Node(val, val, val, arr[low])
            return
        mid = (low + high) // 2
        self.build(2 * pos + 1, low, mid)
        self.build(2 * pos + 2, mid + 1, high)
        self.tree[pos] = self.merge(self.tree[2 * pos + 1], self.tree[2 * pos + 2])

    def update(self, pos, low, high, index, val):
        if index<low or index>high:
            return
        if low == high:
            value = max(val, 0)
            # arr[low] = val
            self.tree[pos] = Node(value, value, value, val)
            return
        mid = (low + high) // 2
        self.update(2 * pos + 1, low, mid, index, val)
        self.update(2 * pos + 2, mid + 1, high, index, val)
        self.tree[pos] = self.merge(self.tree[2 * pos + 1], self.tree[2 * pos + 2])

    def query(self, pos, qLow, qHigh, low, high):
        # if qHigh<low or qLow>high:
        #     return Node(0, 0, 0, 0)
        # if qLow<=low and high<=qHigh:
        #     return self.tree[pos]
        # mid = (low + high) // 2
        # return self.merge(self.query(2*pos+1, qLow, qHigh, low, mid), self.query(2*pos+2, qLow, qHigh, mid+1, high))
        return self.tree[0].mSum

segtree = SegmentTree(n)
segtree.build(0, 0, n-1)

for q1, q2 in queries:
    segtree.update(0, 0, n-1, q1-1, q2)
    nd = segtree.query(0, 0, n-1, 0, n-1)
    print(nd)