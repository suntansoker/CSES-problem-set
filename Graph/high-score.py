# NOT WORKING, WRONG CODE, NEED TO CHECK

from collections import defaultdict

def main():
    n,m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for _ in range(m)]

    dist = [10 ** 15] * (n+1)
    dist[1] = 0
    adj = defaultdict(list)
    for a,b,c in arr:
        adj[a].append((b, c))

    vis1 = [0] * (n+1)
    vis2 = [0] * (n+1)

    def dfs(node, vis):
        vis[node] = 1
        for it, w in adj[node]:
            if vis[it] == 0:
                dfs(it, vis)
        return

    dfs(1, vis1)
    # print(vis1)
    dfs(n, vis2)
    # print(vis2)

    flag = 0
    for i in range(1, n+1):
        flag = 0
        for edge in arr:
            u = edge[0]
            v = edge[1]
            wt = -edge[2]
            
            if vis1[u]==1 and vis2[v]==1 and dist[u] + wt < dist[v]:
                flag = 1
                dist[v] = dist[u] + wt
                
            
    if flag == 1:
        print(-1)
    else:
        print(-1 * dist[n])
    return

if __name__=='__main__':
    main()
        
