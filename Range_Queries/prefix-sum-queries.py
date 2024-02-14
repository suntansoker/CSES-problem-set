import math

class Node:
    def __init__(self):
        self.prefix = 0
        self.sum = 0

n, q = map(int, input().split())

ar = [0]+ [int(x) for x in input().split()]

# x = math.ceil(math.log2(n))

# Seg tree max size
# max_size = 2 * (2 ** x) - 1
st = [Node() for _ in range(4 * n +1)]

def mergeResult(si):
    st[si].sum = st[2 * si].sum + st[2 * si + 1].sum
    st[si].prefix = max(st[2 * si].prefix, st[2 * si].sum + st[2 * si + 1].prefix)

def build(si, ss, se):
    if ss == se:
        st[si].prefix = st[si].sum = ar[ss]
        return
    
    mid = (ss + se) // 2
    build(2 * si, ss, mid)
    build(2 * si + 1, mid + 1, se)
    mergeResult(si)

def update(si, ss, se, qi, val):
    if qi < ss or qi > se:
        return
    
    if ss == se == qi:
        st[si].sum = st[si].prefix = ar[ss] = val
        return
    
    mid = (ss + se) // 2
    update(2 * si, ss, mid, qi, val)
    update(2 * si + 1, mid + 1, se, qi, val)
    mergeResult(si)

def maxProfit(si, ss, se, L, R):
    if ss > R or se < L:
        return Node()
    
    if ss >= L and se <= R:
        return st[si]
    
    mid = (ss + se) // 2
    l = maxProfit(2 * si, ss, mid, L, R)
    r = maxProfit(2 * si + 1, mid + 1, se, L, R)
    res = Node()
    res.sum = l.sum + r.sum
    res.prefix = max(l.prefix, l.sum + r.prefix)
    return res


build(1, 1, n)

for _ in range(q):
    code, *args = map(int, input().split())
    if code == 1:
        k, u = args
        update(1, 1, n, k, u)
    else:
        a, b = args
        print(max(0, maxProfit(1, 1, n, a, b).prefix))
