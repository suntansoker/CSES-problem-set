t = int(input())

MOD = 1000000007

while t>0:
    n = int(input())

    dp = [[0 for _ in range(2)] for _ in range(n+1)]
    dp[n][0], dp[n][1] = 1, 1

    for i in range(n-1, 0, -1):
        dp[i][0] = (2 * dp[i+1][0] + dp[i+1][1]) % MOD
        dp[i][1] = (4 * dp[i+1][1] + dp[i+1][0]) % MOD

    print((dp[1][0] + dp[1][1]) % MOD)

    t -= 1