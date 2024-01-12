n, x = map(int, input().split())
gond = sorted(int(y) for y in input().split())


count = 0
sm = 0

i, j = 0, n-1
while i <= j:
    if i == j:
        count += 1
        break
    else:
        if gond[i] + gond[j] > x:
            count += 1
            j -= 1
        else:
            count += 1
            i += 1
            j -= 1

print(count)
