from collections import defaultdict

n, x = map(int,input().split())
arr = list(map(int, input().split()))

mp = defaultdict(int)

mp[0] = 1
ans = 0
sm = 0

for a in arr:
    sm += a
    if sm-x in mp:
        ans += mp[sm-x]
    mp[sm] += 1

print(ans)


