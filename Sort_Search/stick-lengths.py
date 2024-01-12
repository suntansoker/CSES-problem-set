n = int(input())
arr = sorted(int(y) for y in input().split())

val = arr[n//2]

sm = 0
for i in range(n):
    sm += abs(arr[i] - val)

print(sm)

