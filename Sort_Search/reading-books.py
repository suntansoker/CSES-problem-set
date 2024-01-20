n = int(input())
arr = sorted(list(map(int, input().split())))

sm = 0
for a in arr:
    sm += a

print(max(sm, 2 * arr[-1]))

