import sys
sys.setrecursionlimit(1<<30)
from collections import defaultdict
n = int(input())
arr = [int(x) for x in input().split()]


empl = 2
dp = [0] * (n+1)
vis = [0] * (n+1)

adj = defaultdict(list)

for boss in arr:
    adj[boss].append(empl)
    empl += 1

def dfs(boss):
    vis[boss] = 1
    val = 0
    for employee in adj[boss]:
        if vis[employee] == 0:
            dfs(employee)
            val += 1 + dp[employee]

    dp[boss] = val


dfs(1)

print((' ').join(str(x) for x in dp[1:]))