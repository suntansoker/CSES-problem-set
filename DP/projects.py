from bisect import bisect_left

n = int(input())

arr = []

for _ in range(n):
    start, end, reward = map(int, input().split())
    arr.append((end, start, reward))

arr.sort()

mp = {0:0}
maxReward = 0

for each in arr:
    end, start, reward  = each
    a = list(mp.keys())

    pos = bisect_left(a, start)
    pos -= 1

    totalReward = mp[a[pos]] + reward
    maxReward = max(totalReward, maxReward)
    mp[end] = maxReward

print(maxReward)


