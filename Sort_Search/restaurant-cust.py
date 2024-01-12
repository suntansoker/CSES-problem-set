n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.extend([(x, 1), (y, -1)])

a.sort()

m = 0
cur = 0
i = 0

for _, val in a:
    cur += val
    m = max(cur, m)

print(m)
