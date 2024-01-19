from collections import deque

n, m = map(int, input().split())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

mat = [[x for x in input()] for _ in range(n)]
dis = [[-1 for _ in range(m)] for _ in range(n)]

startR, startC = -1, -1

q = deque()

for i in range(n):
    for j in range(m):
        if mat[i][j] == 'M':
            q.append((0, i, j))
        elif mat[i][j] == 'A':
            startR, startC = i, j

while q:
    dist, r, c = q.popleft()
    if r<0 or r>n-1 or c<0 or c>m-1 or mat[r][c] == '#' or dis[r][c] != -1:
        continue
    dis[r][c] = dist
    for i in range(4):
        q.append((dist+1, r+dx[i], c+dy[i]))

q.append((startR, startC, 0, -1))
d = [[-1 for _ in range(m)] for _ in range(n)]
prev = [[-1 for _ in range(m)] for _ in range(n)]

ans = ''

found = False
while q:
    r, c, dist, di = q.popleft()
    if r<0 or r>n-1 or c<0 or c>m-1 or mat[r][c] == '#' or d[r][c] != -1 or (dis[r][c]>=0 and dis[r][c] <= dist):
        continue
    if r==0 or r==n-1 or c==0 or c==m-1:
        found = True
        d[r][c] = dist
        prev[r][c] = di
        while r!=startR or c!=startC:
            if prev[r][c] == 0:
                ans = 'L' + ans
                c += 1
            elif prev[r][c] == 1:
                ans = 'U' + ans
                r += 1
            elif prev[r][c] == 2:
                ans = 'R' + ans
                c -= 1
            elif prev[r][c] == 3:
                ans = 'D' + ans
                r -= 1

        break

    d[r][c] = dist
    prev[r][c] = di

    for i in range(4):
        q.append((r+dx[i], c+dy[i],dist+1, i))

if found:
    print("YES")
    print(len(ans))
    print(ans)
else:
    print("NO")

    

