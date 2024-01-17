from collections import deque

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]


a = [0, -1, 0, 1]
b = [-1, 0, 1, 0]


startRow, startCol, endRow, endCol = 0, 0, 0, 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'A':
            startRow = i
            startCol = j
        elif mat[i][j] == 'B':
            endRow = i
            endCol = j

q = deque()
q.append((0, -2, startRow, startCol))

vis = [[0 for _ in range(m)] for _ in range(n)]

prev = [[-1 for _ in range(m)] for _ in range(n)]
prev[startRow][startCol] = -2

minDist = 10 ** 9

def findShortestPath(q, endRow, endCol):
    global minDist
    while len(q)>0:
        dist, di, x, y = q.popleft()
        vis[x][y] = 1
        prev[x][y] = di
        if x==endRow and y == endCol:
            minDist = dist
            break
        for i in range(len(a)):
            pos_x = x + a[i]
            pos_y = y + b[i]
            if 0<=pos_x<n and 0<=pos_y<m and vis[pos_x][pos_y] == 0 and mat[pos_x][pos_y] != '#':
                q.append((dist+1, i, pos_x, pos_y))

    ans = ''

    if prev[endRow][endCol] == -1:
        return ans

    while True:
        val = prev[endRow][endCol]
        if val == 0:
            ans = 'L' + ans
            endCol += 1
        elif val == 1:
            ans = 'U' + ans
            endRow += 1
        elif val == 2:
            ans = 'R' + ans
            endCol -= 1
        elif val == 3:
            ans = 'D' + ans
            endRow -= 1
        else:
            break
        

    return ans

ans = findShortestPath(q, endRow, endCol)

if ans == '':
    print("NO")
else:
    print("YES")
    print(minDist)
    print(ans)



