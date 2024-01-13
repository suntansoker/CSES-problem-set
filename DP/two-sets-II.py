n = int(input())

MOD = 1000000007

sm = (n* (n+1)) // 2

if sm % 2 != 0:
    print(0)

else:
    sm //= 2
    dp = [[-1 for _ in range(sm+1)] for _ in range(n+1)]

    def findWays(idx, left):
        if left<0:
            return 0
        if idx==0:
            if left == 0:
                return 1
            else:
                return 0
        
        if dp[idx][left] != -1:
            return dp[idx][left]

        take, notTake = 0, 0
        take = findWays(idx-1, left-idx)
        notTake = findWays(idx-1, left)

        dp[idx][left] = (take+notTake)
        return dp[idx][left]

    print((findWays(n, sm) // 2))




