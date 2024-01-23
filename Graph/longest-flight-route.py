from collections import defaultdict
import heapq

n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(m)]

# with open('test_input.txt', 'r') as file:
#     n, m = map(int, file.readline().split())
#     arr = [[int(x) for x in file.readline().split()] for _ in range(m)]

adj = defaultdict(list)

for u, v in arr:
    adj[u].append((v, -1))

INF = 10 ** 18

dist = [INF] * (n+1)

pq = []

pq.append((0, 1))

par = [-1] * (n+1)

final = []

while pq:
    dis, node = heapq.heappop(pq)
    for it, d in adj[node]:
        if dist[it] > dis + d:
            dist[it] = dis + d
            heapq.heappush(pq, (dist[it], it))
            par[it] = node

if dist[n] == INF:
    print("IMPOSSIBLE")
else:
    t = n
    ans = []
    while t != -1:
        ans.append(t)
        t = par[t]

    print(len(ans))
    print(' '.join(str(x) for x in reversed(ans)))