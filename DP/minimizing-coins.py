n, x = map(int, input().split())
arr = [int(y) for y in input().split()]
INF = 10 ** 10

dp = [INF for _ in range(x+1)]

dp[0] = 0

for i in range(1, x+1):
    for j in arr:
        if i-j>=0:
            dp[i] = min(dp[i], 1+dp[i-j])

if dp[x] >= INF:
    print(-1)
else:
    print(dp[x])
