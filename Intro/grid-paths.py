st = input()

x = [0, -1, 0, 1]
y = [-1, 0, 1, 0]


# for dx, dy in zip(x, y):
#     print(dx, dy)

vis = [[0 for _ in range(7)] for _ in range(7)]

def solve(row, col, idx):
    if idx == len(st):
        if row==6 and col == 0:
            return 1
        else:
            return 0
    if row==6 and col ==0:
        return 0

    if vis[row][col] == 1:
        return 0

    visited = [0] * 4 

    LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3
    

    for i in range(4):
        if 0<=row+x[i]<7 and 0<=col+y[i]<7:
            visited[i] = vis[row+x[i]][col+y[i]]
    
    TOP_LEFT = [row-1,col-1]
    TOP_RIGHT = [row-1,col+1]
    BOTTOM_LEFT = [row+1,col-1]
    BOTTOM_RIGHT = [row+1,col+1] 

    if visited[LEFT]==0 and visited[RIGHT]==0 and visited[UP]==1 and visited[DOWN]==1:
        return 0
    
    if visited[UP]==0 and visited[DOWN]==0 and visited[LEFT]==1 and visited[RIGHT]==1:
        return 0

    if 0<=TOP_LEFT[0]<7 and 0<=TOP_LEFT[1]<7 and vis[TOP_LEFT[0]][TOP_LEFT[1]]==1:
        if visited[LEFT]==0 and visited[UP]==0:
            return 0

    if 0<=TOP_RIGHT[0]<7 and 0<=TOP_RIGHT[1]<7 and vis[TOP_RIGHT[0]][TOP_RIGHT[1]]==1:
        if visited[UP]==0 and visited[RIGHT]==0:
            return 0

    if 0<=BOTTOM_LEFT[0]<7 and 0<=BOTTOM_LEFT[1]<7 and vis[BOTTOM_LEFT[0]][BOTTOM_LEFT[1]]==1:
        if visited[LEFT]==0 and visited[DOWN]==0:
            return 0

    if 0<=BOTTOM_RIGHT[0]<7 and 0<=BOTTOM_RIGHT[1]<7 and vis[BOTTOM_RIGHT[0]][BOTTOM_RIGHT[1]]==1:
        if visited[RIGHT]==0 and visited[DOWN]==0:
            return 0

    vis[row][col] = 1

    ans = 0

    if st[idx] == '?':
        for i in range(4):
            if 0<=row+x[i]<7 and 0<=col+y[i]<7:
                ans += solve(row+x[i], col+y[i], idx+1)
    else:
        if st[idx]=='U' and 0<=row-1<7 and 0<=col<7:
            ans += solve(row-1, col, idx+1)
        elif st[idx]=='R' and 0<=row<7 and 0<=col+1<7:
            ans += solve(row, col+1, idx+1)
        elif st[idx]=='D' and 0<=row+1<7 and 0<=col<7:
            ans += solve(row+1, col, idx+1)
        elif st[idx]=='L' and 0<=row<7 and 0<=col-1<7:
            ans += solve(row, col-1, idx+1)

    vis[row][col] = 0

    return ans


print(solve(0, 0, 0))