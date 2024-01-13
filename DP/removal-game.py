n = int(input())
arr = [int(y) for y in input().split()]

dp = [[-1 for _ in range(n)] for _ in range(n)]

def findMaxScore(left, right):
    if left>right:
        return 0
    if left == right:
        return arr[left]
    if dp[left][right] != -1:
        return dp[left][right]
    ifLeft = arr[left] - findMaxScore(left+1, right)
    ifRight = arr[right] - findMaxScore(left, right-1)
    dp[left][right] = max(ifLeft, ifRight)
    return dp[left][right]

print((sum(arr)+ findMaxScore(0, n-1)) // 2)