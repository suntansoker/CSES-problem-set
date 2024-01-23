from collections import defaultdict
import heapq

n, m = map(int, input().split())
edges = [[int(x) for x in input().split()] for _ in range(m)]
# with open('test_input.txt', 'r') as file:
#     n, m = map(int, file.readline().split())
#     edges = [[int(x) for x in file.readline().split()] for _ in range(m)]

adj = defaultdict(list)

for a, b, c in edges:
    adj[a].append((b, c))

MOD = 1000000007

dist = [10 ** 15] * (n+1)
min_flights = [0] * (n+1)
max_flights = [0] * (n+1)
routes = [0] * (n+1)

dist[1] = 0
routes[1] = 1


pq = []
heapq.heappush(pq, (0, 1))

while pq:
    dis, u = heapq.heappop(pq)
    for v, adjDist in adj[u]:
        if dis + adjDist == dist[v]:
            routes[v] += routes[u]
            routes[v] %= MOD
            min_flights[v] = min(min_flights[u]+1, min_flights[v])
            max_flights[v] = max(max_flights[u]+1, max_flights[v])

        elif dis + adjDist < dist[v]:
            dist[v] = dis + adjDist
            routes[v] = routes[u]
            min_flights[v] = min_flights[u]+1
            max_flights[v] = max_flights[u]+1
            heapq.heappush(pq, (dist[v], v))

print(str(dist[n]) + ' ' + str(routes[n]) + ' ' + str(min_flights[n]) + ' ' + str(max_flights[n]))
    