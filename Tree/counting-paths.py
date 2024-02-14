from collections import defaultdict
import sys

sys.setrecursionlimit(1<<30)

n, q = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(n-1)]
queries = [[int(x) for x in input().split()] for _ in range(q)]

# with open('test_input.txt', 'r') as file:
#     n, q = map(int, file.readline().split())
#     arr = [[int(x) for x in file.readline().split()] for _ in range(n-1)]
#     queries = [[int(x) for x in file.readline().split()] for _ in range(q)]
depth = [0] * (n+1)
# this is the difference arr, so we add 1 at the start and -1 at the index after the end. At the end, we do a prefix sum to get the count of visits
ans = [0] * (n+1) 

MAXDIST, MAXN = 20, n+1

routes = [[-1 for _ in range(MAXDIST)] for _ in range(MAXN)]
adj = defaultdict(list)

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

def dfs_for_sum(node, par):
    x = ans[node]
    for it in adj[node]:
        if it != par:
            dfs_for_sum(it, node)
            x += ans[it]
    
    ans[node] = x

findDepth(1, 0, -1)
propagate()

for q1, q2 in queries:
    lca = findLCA(q1, q2)
    ans[q1] += 1
    ans[q2] += 1
    ans[lca] -= 1
    if routes[lca][0] != -1:
        # Subtracting an extra 1 from the parent of the lca, to nullify the effect of addition of 1
        ans[routes[lca][0]] -= 1

dfs_for_sum(1, 0)

print(' '.join(str(x) for x in ans[1:]))









