from collections import defaultdict

n, m = map(int, input().split())
courses = [[int(x) for x in input().split()] for _ in range(m)]

inDegree = [0] * (n+1)
adj = defaultdict(list)

for c1, c2 in courses:
    inDegree[c2] += 1
    adj[c1].append(c2)

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

if len(topoSort) < n:
    print("IMPOSSIBLE")
else:
    print(' '.join(str(x) for x in topoSort))
