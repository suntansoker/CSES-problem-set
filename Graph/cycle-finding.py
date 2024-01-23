n, m = map(int, input().split())
edges = [[int(x) for x in input().split()] for _ in range(m)]

dist = [0] * (n+1)
parent = [-1] * (n+1)

for i in range(1, n+1):
    x = -1
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            x = v
            parent[v] = u

if x == -1:
    print("NO")
else:
    # print(parent)
    # # print(x)

    # This loop makes sure that we start from a node in the negative cycle
    for i in range(1, n+1):
        x = parent[x]
    # print(parent)
    # print(x)

    arr = []
    p = x
    while(True):
        arr.append(x)
        if p == x and len(arr) > 1:
            break
        x = parent[x]

    print("YES")
    print(' '.join(str(x) for x in reversed(arr)))



