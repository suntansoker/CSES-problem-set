import sys
sys.setrecursionlimit(1<<30)
from collections import defaultdict
n = int(input())
arr = [[int(x) for x in input().split()] for _ in range(n-1)]

# with open('test_input.txt', 'r') as file:
#     n = int(file.readline())
#     arr = [[int(x) for x in file.readline().split()] for _ in range(n-1)]

dp = [[-1 for _ in range(2)] for _ in range(n+1)]
adj = defaultdict(list)

for e1, e2 in arr:
    adj[e1].append(e2)
    adj[e2].append(e1)

def findMax(node, par, included):
    if dp[node][included] != -1:
        return dp[node][included]
    
    # So for every node there are two options:
    # Either we dont include the node, so we include its connecting nodes
    # Or we include the node, then we choose one of the edges
    if included:
        val = 0
        for it in adj[node]:
            if it != par:
                val += findMax(it, node, 1)

        res = 0
        # time to include one edge one by one (i,e make included for the neighbouring node to be 0, so that it can't group with its children nodes)
        for it in adj[node]:
            if it!= par:
                res = max(res, val - dp[it][1] + 1 + findMax(it, node, 0))

        dp[node][included] = res
    else:
        val = 0
        for it in adj[node]:
            if it != par:
                val += findMax(it, node, 1)

        dp[node][included] = val

    return dp[node][included]

print(max(findMax(1, -1, 0), findMax(1, -1, 1)))


