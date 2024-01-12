n = int(input())
arr = list(int(y) for y in input().split())

past = 0
best =  - (10 ** 15) 

for i in range(n):
    if past + arr[i] >= arr[i]:
        past += arr[i]
    else:
        past = arr[i]
    best = max(best, past)

print(best)
