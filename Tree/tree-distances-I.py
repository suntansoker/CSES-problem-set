import sys
sys.setrecursionlimit(1<<30)
from collections import defaultdict
n = int(input())
arr = [[int(x) for x in input().split()] for _ in range(n-1)]

# with open('test_input.txt', 'r') as file:
#     n = int(file.readline())
#     arr = [[int(x) for x in file.readline().split()] for _ in range(n-1)]

depth = [0] * (n+1)
dp = [-1] * (n+1)

adj = defaultdict(list)

MIN = - (10 ** 15)

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

def findDistances(node, parent, p_dist):
    if dp[node] != -1:
        return dp[node]
    prefMax, sufMax = [], []
    for it in adj[node]:
        if it != parent:
            prefMax.append(depth[it])
            sufMax.append(depth[it])
    
    for i in range(1, len(prefMax)):
        prefMax[i] = max(prefMax[i-1], prefMax[i])

    for i in range(len(sufMax)-2, -1, -1):
        sufMax[i] = max(sufMax[i+1], sufMax[i])

    childNo = 0

    for it in adj[node]:
        mx1, mx2 = MIN, MIN
        if it != parent:
            if childNo == 0 and childNo+1<len(sufMax):
                mx1 = MIN
                mx2 = sufMax[childNo+1]
            elif childNo == len(prefMax)-1 and childNo-1>=0:
                mx1 = prefMax[childNo-1]
                mx2 = MIN
            elif childNo-1>=0 and childNo+1<len(sufMax):
                mx1 = prefMax[childNo-1]
                mx2 = sufMax[childNo+1]

            part_dist = 1 + max(p_dist, max(mx1, mx2))
            findDistances(it, node, part_dist)
            childNo += 1

    val = 0
    if len(prefMax) == 0:
        val = -1
    else:
        val = prefMax[-1]
    dp[node] = 1 + max(p_dist, val)
    return dp[node]

findDepth(1, 0)
findDistances(1, 0, -1)

print(' '.join(str(x) for x in dp[1:]))