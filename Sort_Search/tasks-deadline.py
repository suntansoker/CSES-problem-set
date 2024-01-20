n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

ans = 0
t = 0
for f, d in arr:
    t += f
    ans += d - t

print(ans)



