import sys
input = sys.stdin.readline
 
n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]
 
class Node:
    def __init__(self, lazystart=0, lazydelta=0, sum=0):
        self.lazystart = lazystart 
        self.lazydelta = lazydelta 
        self.sum = sum
 
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [Node() for _ in range(4 * self.n)]
 
    # def merge(self, leftSum, rightSum):
    #     return leftSum + rightSum
 
    def build(self, pos, low, high):
        if low == high:
            self.tree[pos].sum = arr[low]
            return
        mid = (low + high) >> 1
        self.build(2 * pos + 1, low, mid)
        self.build(2 * pos + 2, mid + 1, high)
        self.tree[pos].sum = self.tree[2 * pos + 1].sum + self.tree[2 * pos + 2].sum
    
    def pushdown(self, pos, l, r):
        if self.tree[pos].lazystart != 0 or self.tree[pos].lazydelta != 0:
            interval = r - l + 1
            self.tree[pos].sum += interval * (self.tree[pos].lazystart) + self.tree[pos].lazydelta * ((interval * (interval + 1)) // 2)
            if l < r:
                mid = (l + r) // 2
                leftInterval = mid - l + 1
                rightInterval = r - mid
                self.tree[2*pos+1].lazystart += self.tree[pos].lazystart
                self.tree[2*pos+1].lazydelta += self.tree[pos].lazydelta
                self.tree[2*pos+2].lazystart += self.tree[pos].lazystart + leftInterval * self.tree[pos].lazydelta
                self.tree[2*pos+2].lazydelta += self.tree[pos].lazydelta
            self.tree[pos].lazystart = 0
            self.tree[pos].lazydelta = 0
        return
 
    def update(self, pos, low, high, uLow, uHigh, valStart, delta):
        self.pushdown(pos, low, high)
        if uHigh<low or uLow>high:
            return
        if uLow<=low and high<=uHigh:
            self.tree[pos].lazystart += valStart + low - uLow
            self.tree[pos].lazydelta += delta
            self.pushdown(pos, low, high)
            return
        mid = (low + high) >> 1
        self.update(2 * pos + 1, low, mid, uLow, uHigh, valStart, delta)
        self.update(2 * pos + 2, mid + 1, high, uLow, uHigh, valStart, delta)
        self.tree[pos].sum = self.tree[2 * pos + 1].sum + self.tree[2 * pos + 2].sum
 
    def query(self, pos, qLow, qHigh, low, high):
        if qHigh<low or qLow>high:
            return 0
        self.pushdown(pos, low, high)
        if qLow<=low and high<=qHigh:
            return self.tree[pos].sum
        mid = (low + high) >> 1
        return self.query(2*pos+1, qLow, qHigh, low, mid) + self.query(2*pos+2, qLow, qHigh, mid+1, high)
 
segtree = SegmentTree(n)
segtree.build(0, 0, n-1)
 
for i in range(q):
    q1 = queries[i][0]
    q2 = queries[i][1] - 1
    q3 = queries[i][2] - 1
    if q1 == 1:
        segtree.update(0, 0, n-1, q2, q3, 0, 1)
    else: 
        print(segtree.query(0, q2, q3, 0, n-1))
