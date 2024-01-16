t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    if max(a, b)<=2 * min(a, b) and ((a+b) % 3 ==0):
        print("YES")
    else:
        print("NO")