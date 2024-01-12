n = int(input())

dp = [0 for _ in range(n+1)]
dp[0], dp[1] = 1, 1 

for i in range(2, n+1):
    for j in range(1, 7):
        if i-j>=0:
            dp[i] += dp[i-j] % 1000000007

print(dp[n] % 1000000007)