import sys
sys.setrecursionlimit(1<<30)
from collections import defaultdict
n = int(input())
arr = [[int(x) for x in input().split()] for _ in range(n-1)]

depth = [0] * (n+1)

adj = defaultdict(list)

diameter = [0] * (n+1)

for e1, e2 in arr:
    adj[e1].append(e2)
    adj[e2].append(e1)

def findDepth(node, par):
    isLeaf = True
    dist = 0
    for it in adj[node]:
        if it != par:
            isLeaf = False
            findDepth(it, node)
            dist = max(dist, depth[it])

    if isLeaf:
        depth[node] = 0
    else:
        depth[node] = 1 + dist

def findDiameter(node, parent):
    ans = 0
    paths = []
    for it in adj[node]:
        if it != parent:
            findDiameter(it, node)
            paths.append(depth[it])
            ans = max(ans, diameter[it])
    # print(paths)
    paths.sort(reverse=True)
    if len(paths) == 0:
        diameter[node] = 0
    elif len(paths) == 1:
        diameter[node] = 1 + paths[0]
    else:
        diameter[node] = 2 + paths[0] + paths[1]

    diameter[node] = max(ans, diameter[node])


findDepth(1, 0)

findDiameter(1, 0)

print(diameter[1])
