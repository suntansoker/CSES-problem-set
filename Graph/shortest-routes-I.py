from collections import defaultdict
import heapq

n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(m)]

adj = defaultdict(list)
for a, b, c in arr:
    adj[a].append((b, c))

res = [10 ** 15] * (n+1)
res[1] = 0

pq = []
heapq.heappush(pq, (0, 1))

while pq:
    dist, node = heapq.heappop(pq)
    for adjNode, adjDist in adj[node]:
        if dist + adjDist < res[adjNode]:
            res[adjNode] = dist + adjDist
            heapq.heappush(pq, (res[adjNode], adjNode))

print(' '.join(str(x) for x in res[1:]))

    


