import bisect

n, m = map(int, input().split())
tick = sorted(int(x) for x in input().split())
max_cust = list(int(x) for x in input().split())

tick.sort()

for i in range(m):
    idx = bisect.bisect_right(tick, max_cust[i])
    if idx <= 0:
        print(-1)
    else:
        idx -= 1
        print(tick[idx])
        del tick[idx]
