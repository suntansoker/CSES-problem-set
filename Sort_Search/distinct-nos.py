n = int(input())
arr = sorted(int(x) for x in input().split())

s = set()

for i in range(n):
    s.add(arr[i])

ans = len(s)

print(ans)
