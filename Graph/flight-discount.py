from collections import defaultdict
import heapq

n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(m)]

adj1 = defaultdict(list)
adj2 = defaultdict(list)

for a, b, c in arr:
    adj1[a].append((b, c))
    adj2[b].append((a, c))

res1 = [10 ** 15] * (n+1)
res1[1] = 0

res2 = [10 ** 15] * (n+1)
res2[n] = 0

pq1 = []
heapq.heappush(pq1, (0, 1))

while pq1:
    dist, node = heapq.heappop(pq1)
    for adjNode, adjDist in adj1[node]:
        if dist + adjDist < res1[adjNode]:
            res1[adjNode] = dist + adjDist
            heapq.heappush(pq1, (res1[adjNode], adjNode))

pq2 = []
heapq.heappush(pq2, (0, n))

while pq2:
    dist, node = heapq.heappop(pq2)
    for adjNode, adjDist in adj2[node]:
        if dist + adjDist < res2[adjNode]:
            res2[adjNode] = dist + adjDist
            heapq.heappush(pq2, (res2[adjNode], adjNode))

cheapest = 10 ** 15
for a, b, c in arr:
    if res1[a] + res2[b] + c // 2 < cheapest:
        cheapest = res1[a] + res2[b] + c // 2

print(cheapest)