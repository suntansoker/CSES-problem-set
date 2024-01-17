from collections import defaultdict, deque

n, m = map(int, input().split())
arr = [[int(x) for x in input().split()] for _ in range(m)]

adj = defaultdict(list)

for a1, a2 in arr:
    adj[a1].append(a2)
    adj[a2].append(a1)

q = deque()
ans = []
q.append((1, 1, [1]))
vis = [0] * (n+1)


def bfs(q, ans):
    while len(q)>0:
        time, node, path = q.popleft()
        vis[node] = 1
        ans.append(node)
        if node==n:
            return path, time
        for it in adj[node]:
            if vis[it]==0:
                q.append((time+1, it, path + [it]))

    return [], 0

        

path, time = bfs(q, ans)
if len(path) == 0:
    print("IMPOSSIBLE")
else:
    print(time)

    print(' '.join([str(x) for x in path]))