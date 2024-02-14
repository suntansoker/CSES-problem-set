from collections import defaultdict
import sys

sys.setrecursionlimit(1<<30)

n, q = map(int, input().split())
arr = input().split()

queries = [[int(x) for x in input().split()] for _ in range(q)]
depth = [0] * (n+1)

MAXDIST, MAXN = 20, n+1
routes = [[-1 for _ in range(MAXDIST)] for _ in range(MAXN)]
adj = defaultdict(list)

for i in range(1, n):
    routes[i+1][0] = int(arr[i-1])
    adj[int(arr[i-1])].append(i+1)

for d in range(1, MAXDIST):
    for i in range(1, MAXN):
        if routes[i][d-1] != -1:
            routes[i][d] = routes[routes[i][d-1]][d-1]


def findDepth(node,dist):
    depth[node] = dist
    for it in adj[node]:
        findDepth(it, dist+1)

def findLCA(q1, q2):
    if depth[q1]>depth[q2]:
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

findDepth(1,0)

for q1, q2 in queries:
    print(findLCA(q1, q2))







