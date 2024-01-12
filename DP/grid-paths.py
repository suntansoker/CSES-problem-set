n = int(input())
arr = []

for _ in range(n):
    arr.append(list(input()))

dp = [[0 for _ in range(n)] for _ in range(n)]

if arr[0][0]=='.':
    dp[0][0] = 1

for j in range(1, n):
    if arr[0][j] == '.':
        dp[0][j] = (dp[0][j] + dp[0][j-1]) % 1000000007
    else:
        dp[0][j] = 0

for i in range(1, n):
    if arr[i][0] == '.':
        dp[i][0] = (dp[i][0] +dp[i-1][0]) % 1000000007
    else:
        dp[i][0] = 0

for i in range(1, n):
    for j in range(1, n):
        if arr[i][j] == '.':
            dp[i][j] = (dp[i][j] + dp[i-1][j] + dp[i][j-1]) % 1000000007
        else:
            dp[i][j] = 0

print(dp[n-1][n-1])



