n, x = map(int, input().split())
price = [int(y) for y in input().split()]
pages = [int(z) for z in input().split()]

dp = [[0 for _ in range(x+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,x+1):
        dp[i][j] = dp[i-1][j]
        if j-price[i-1] >= 0:
            dp[i][j] = max(dp[i][j], pages[i-1] + dp[i-1][j-price[i-1]])

print(dp[n][x])