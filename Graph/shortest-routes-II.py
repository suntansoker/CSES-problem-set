n,m,q = map(int, input().split())

arr = [[int(x) for x in input().split()] for _ in range(m)]
queries = [[int(x) for x in input().split()] for _ in range(q)]

mat = [[10 ** 15 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    mat[i][i] = 0

for a, b, c in arr:
    mat[a][b] = min(mat[a][b],c)
    mat[b][a] = min(mat[b][a],c)

for k in range(0, n+1):
    for i in range(0, n+1):
        for j in range(0, n+1):
            mat[i][j] = min(mat[i][j], mat[i][k]+mat[k][j])

for q1, q2 in queries:
    if mat[q1][q2] >= 10 ** 15:
        print(-1)
    else:
        print(mat[q1][q2])

