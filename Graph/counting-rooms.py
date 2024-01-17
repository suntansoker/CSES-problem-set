n, m = map(int, input().split())

mat = [[x for x in input()] for _ in range(n)]

count = 0
vis = set()

a = [0, -1, 0, 1]
b = [-1, 0, 1, 0]

def bfs(x, y):
    q = []
    q.append((x, y))

    while len(q)>0:
        i, j = q.pop(0)
        vis.add((i, j))
        for dx, dy in zip(a, b):
            new_x, new_y = i+dx, j+dy
            if 0<=new_x<n and 0<=new_y<m and (new_x, new_y) not in vis and mat[new_x][new_y] == '.':
                q.append((new_x,new_y))
    
    return

for i in range(n):
    for j in range(m):
        if (i, j) not in vis and mat[i][j] == '.':
            count += 1
            bfs(i, j)

print(count)