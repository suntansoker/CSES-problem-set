# NEED TO UNDERSTAND

from collections import defaultdict

# n, m = map(int, input().split())
# edges = [[int(x) for x in input().split()] for _ in range(m)]

with open('test_input.txt', 'r') as file:
    n, m = map(int, file.readline().split())
    edges = [[int(x) for x in file.readline().split()] for _ in range(m)]

MOD = 1000000007

inDegree = [0] * (n+1)
dp = [0] * (n+1)
adj = defaultdict(list)
back = defaultdict(list)

dp[1] = 1

for c1, c2 in edges:
    inDegree[c2] += 1
    adj[c1].append(c2)
    back[c2].append(c1)

q = []
for i in range(1, n+1):
    if inDegree[i] == 0:
        q.append(i)

topoSort = []

while q:
    node = q.pop(0)
    topoSort.append(node)
    for it in adj[node]:
        inDegree[it] -= 1
        if inDegree[it] == 0:
            q.append(it)

    for backnode in back[node]:
        dp[node] = (dp[backnode] + dp[node]) % MOD

print(dp[n])
