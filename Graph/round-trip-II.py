from collections import defaultdict, deque
import sys

def main():
    n, m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for _ in range(m)]

    adj = defaultdict(list)

    sys.setrecursionlimit(7500)

    for a1, a2 in arr:
        adj[a1].append(a2)

    vis = [0] * (n+1)

    def detectCycle(node, par, vis, path):
        vis[node] = 1
        for it in adj[node]:
            if vis[it] == 0:
                pat = detectCycle(it, node, vis, path+[it])
                if len(pat) == 0:
                    continue
                else:
                    # print("Here1:",path)
                    # print(it)
                    # print("-=-=-=")
                    return pat
            elif it in path:
                # print("Here2:",path)
                # print(it)
                # print("-=-=-=")
                return path + [it]

        return []



    for i in range(1, n+1):
        if vis[i] == 0:
            path = detectCycle(i, -1, vis, [i])
            if len(path) > 0:
                i, j = len(path)-1, 0
                while j<i:
                    if path[j] == path[i]:
                        break
                    j += 1
                print(i-j+1)
                print(' '.join([str(x) for x in path[j:]]))
                return
                
    print("IMPOSSIBLE")
    return


if __name__=='__main__':
    main()