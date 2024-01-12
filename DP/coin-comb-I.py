n, x = map(int, input().split())
arr = [int(y) for y in input().split()]

dp = [0 for _ in range(x+1)]

dp[0] = 1

for i in range(1, x+1):
    for j in arr:
        if i-j>=0:
            dp[i] = (dp[i] + dp[i-j]) % 1000000007

print(dp[x])
