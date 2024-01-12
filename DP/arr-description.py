n, m = map(int, input().split())
arr = [int(y) for y in input().split()]

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

# dp[i][j] = Number of arrays of length i with last number as j

# Base case
for i in range(1, m+1):
    if arr[0] == 0 or arr[0]==i:
        dp[1][i] = 1

for i in range(2, n+1):
    for j in range(1, m+1):
        if arr[i-1] != 0 and arr[i-1] != j:
            dp[i][j] = 0
            continue

        for k in range(j-1, min(m+1, j+2)):
            dp[i][j] = (dp[i][j]+ dp[i-1][k]) % 1000000007

ans = 0
for i in range(1, m+1):
    ans = (ans + dp[n][i]) % 1000000007

print(ans)