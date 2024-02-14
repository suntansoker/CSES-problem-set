from collections import defaultdict
import sys

sys.setrecursionlimit(1<<30)
n, q = map(int, input().split())

arr = [[int(x) for x in input().split()] for _ in range(n-1)]
queries = [[int(x) for x in input().split()] for _ in range(q)]

adj = defaultdict(list)
MAXN, MAXDIST = n+1, 20
routes = [[-1 for _ in range(MAXDIST)] for _ in range(MAXN)]
depth = [0] * (n+1)

for e1, e2 in arr:
    adj[e1].append(e2)
    adj[e2].append(e1)


def findDepth(node, dist, par):
    depth[node] = dist
    for it in adj[node]:
        if it != par:
            routes[it][0] = node
            findDepth(it, dist+1, node)

def propagate():
    for d in range(1, MAXDIST):
        for i in range(1, MAXN):
            if routes[i][d-1] != -1:
                routes[i][d] = routes[routes[i][d-1]][d-1]
                
def findDist(q1, q2):
    if depth[q1] > depth[q2]:
        q1, q2 = q2, q1

    d = depth[q2] - depth[q1]

    for i in range(MAXDIST):
        if d & (1<<i) > 0:
            q2 = routes[q2][i]

    if q1 == q2:
        return q1

    for i in range(MAXDIST-1, -1, -1):
        if routes[q1][i] != routes[q2][i]:
            q1 = routes[q1][i]
            q2 = routes[q2][i]

    return routes[q1][0]

findDepth(1, 0, -1)
propagate()
for q1, q2 in queries:
    lca = findDist(q1, q2)
    print(depth[q1] - depth[lca] + depth[q2] - depth[lca])



