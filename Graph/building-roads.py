from collections import defaultdict

n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(m)]

adj = defaultdict(list)

for a1, a2 in arr:
    adj[a1].append(a2)
    adj[a2].append(a1)

comps = []

vis = [0] * (n+1)
q = []

# def dfs(node):
#     vis[node] = 1

#     for it in adj[node]:
#         if vis[it]==0:
#             dfs(it)

#     return

def bfs(node, q):
    q.append(node)
    while len(q)>0:
        popped = q.pop(0)   
        vis[popped] = 1
        for it in adj[popped]:
            if vis[it] == 0:
                q.append(it)

    return

for i in range(1, n+1):
    if vis[i] == 0:
        q = []
        bfs(i, q)
        comps.append(i)

if len(comps) <= 1:
    print(0)
else:
    print(len(comps)-1)
    for i in range(1, len(comps)):
        print(str(comps[i]) + ' ' + str(comps[i-1]))



