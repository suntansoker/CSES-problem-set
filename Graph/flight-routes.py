import heapq
from collections import defaultdict

n, m ,k = map(int, input().split())
edges = [[int(x) for x in input().split()] for _ in range(m)]

adj = defaultdict(list)

for e1, e2, w in edges:
    adj[e1].append((e2, w))

INF = 10 ** 18

dist = [[INF for _ in range(k)] for _ in range(n+1)]
dist[1][0] = 0

pq = []
pq.append((0, 1))

while pq:
    dis, u = heapq.heappop(pq)
    for v, w in adj[u]:
        if dist[v][k-1] < dis + w:
            continue
        else:
            dist[v][k-1] = dis + w
            heapq.heappush(pq, (dist[v][k-1], v))
            dist[v].sort()

print(' '.join(str(x) for x in dist[n]))



