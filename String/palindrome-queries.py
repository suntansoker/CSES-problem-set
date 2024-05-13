N, Q = map(int, input().split())
s = input().strip()
# operations = [list(map(str, input().split())) for _ in range(Q)]
# Creating hash
HASH = 257
MOD = 10**9 + 7

# Initialize powers of HASH
powH = [1] * 200005
for i in range(1, N):
    powH[i] = (powH[i - 1] * HASH) % MOD

# Forward hash Segment Tree functions
forward_tree = [0] * (4 * N)

def forward_update(i, v):
    i += N
    forward_tree[i] = v
    while i > 1:
        i >>= 1
        forward_tree[i] = (forward_tree[i << 1] + forward_tree[i << 1 | 1]) % MOD

def forward_query(l, r):
    res = 0
    l += N
    r += N + 1
    while l < r:
        if l & 1:
            res = (res + forward_tree[l]) % MOD
            l += 1
        if r & 1:
            r -= 1
            res = (res + forward_tree[r]) % MOD
        l >>= 1
        r >>= 1
    return res

# Backward hash Segment Tree functions
backward_tree = [0] * (4 * N)

def backward_update(i, v):
    i += N
    backward_tree[i] = v
    while i > 1:
        i >>= 1
        backward_tree[i] = (backward_tree[i << 1] + backward_tree[i << 1 | 1]) % MOD

def backward_query(l, r):
    res = 0
    l += N
    r += N + 1
    while l < r:
        if l & 1:
            res = (res + backward_tree[l]) % MOD
            l += 1
        if r & 1:
            r -= 1
            res = (res + backward_tree[r]) % MOD
        l >>= 1
        r >>= 1
    return res

# Preprocess the input string
# s = input().strip()
for i, c in enumerate(s):
    forward_update(i, powH[i] * ord(c) % MOD)
    backward_update(i, powH[N - i - 1] * ord(c) % MOD)

# Process operations
for _ in range(Q):
    t, *args = map(str, input().split())
    if t == '1':
        k, x = int(args[0]), args[1]
        k -= 1
        forward_update(k, powH[k] * ord(x) % MOD)
        backward_update(k, powH[N - k - 1] * ord(x) % MOD)
    elif t == '2':
        l, r = map(int, args)
        l -= 1
        r -= 1
        forward = forward_query(l, r)
        forward = (forward * powH[N - 1 - r]) % MOD
        backward = backward_query(l, r)
        backward = (backward * powH[l]) % MOD
        if forward == backward:
            print("YES")
        else:
            print("NO")
