n = int(input())

INF = 10 ** 8

dp = [INF for _ in range(n+1)]

dp[0] = 0

for i in range(1, n+1):
    for j in str(i):
        dp[i] = min(1+dp[i-int(j)], dp[i])

print(dp[n])
