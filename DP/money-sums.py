n = map(int, input())
arr = [int(y) for y in input().split()]

sm = 0
for s in arr:
    sm += s

dp = [0 for _ in range(sm+1)]
dp[0] = 1

for j in arr:
    for i in range(sm, 0, -1):
        if i-j<0:
            break
        if dp[i] == 1:
            continue
        if dp[i-j] == 1:
            dp[i] = 1

ans = []
for i in range(1, sm+1):
    if dp[i] == 1:
        ans.append(i)

output = ' '.join(str(x) for x in ans)
print(len(ans))
print(output)

