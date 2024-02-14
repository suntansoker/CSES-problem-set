n, q = map(int, input().split())
arr = input().split()

queries = [[int(x) for x in input().split()] for _ in range(q)]

MAXDIST, MAXN = 20, n+1
routes = [[-1 for _ in range(MAXDIST)] for _ in range(MAXN)]

for i in range(1,n):
    routes[i+1][0] = int(arr[i-1])

for d in range(1, MAXDIST):
    for i in range(1, MAXN):
        if routes[i][d-1] != -1:
            routes[i][d] = routes[routes[i][d-1]][d-1]

def findDest(node, dist):
    for i in range(MAXDIST):
        if dist & 1<<i > 0:
            node = routes[node][i]
            if node == -1:
                break

    return node

for q1, q2 in queries:
    print(findDest(q1, q2))