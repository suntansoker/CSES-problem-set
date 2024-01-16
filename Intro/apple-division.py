n = int(input())

arr = [int(x) for x in input().split()]

mn = 10 ** 9

for i in range(1<<n):
    sm1, sm2 = 0, 0
    for j in range(n):
        if 1<<j & i >0:
            sm1 += arr[j]
        else:
            sm2 += arr[j]

    mn = min(mn, abs(sm1-sm2))

print(mn)