n, x = map(int, input().split())
arr = [int(y) for y in input().split()]

INF = 10 ** 9

dp = [[INF, INF] for _ in range(1 << n)]
dp[0][0] = 1
dp[0][1] = 0

for mask in range(1, 1<<n):
    for i in range(n):
        if (mask & 1<<i) > 0:
            prev = mask ^ (1<<i)
            numberofElevators, totalCount = dp[prev]
            # if totalCount + arr[i] <= x:
            #     dp[mask][0] = min(numberofElevators, dp[mask][0])
            #     dp[mask][1] = totalCount + arr[i]
            # else:
            #     dp[mask][0] = numberofElevators + 1
            #     dp[mask][1] = min(dp[mask][1], arr[i])

            if totalCount + arr[i] <= x:
                dp[mask] = min(dp[mask], [numberofElevators, totalCount+arr[i]])
            else:
                dp[mask] = min(dp[mask], [numberofElevators+1, arr[i]])

print(dp[(1<<n) - 1][0])