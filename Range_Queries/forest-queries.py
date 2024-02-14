import math

n, q = map(int, input().split())
arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    arr[i+1][1:] = [1 if x=='*' else 0 for x in input()]
queries = [[int(x) for x in input().split()] for _ in range(q)]

for i in range(1, n+1):
    for j in range(1, n+1):
        arr[i][j] += arr[i][j-1]

for j in range(1, n+1):
    for i in range(1, n+1):
        arr[i][j] += arr[i-1][j]

for r1, c1, r2, c2 in queries:
    print(arr[r2][c2] - arr[r1-1][c2] - arr[r2][c1-1] + arr[r1-1][c1-1])