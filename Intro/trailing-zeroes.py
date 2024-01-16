n = int(input())

i = 1

ans = 0

while pow(5, i) <= n:
    p = pow(5, i)
    ans += n // p
    i += 1

print(ans)