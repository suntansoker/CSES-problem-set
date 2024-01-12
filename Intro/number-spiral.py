def findNo(x, y):
    if x == y:
        print(x ** 2 - (x-1))
    elif x > y:
        diag = x ** 2 - (x-1)
        print(diag + (-1)**x * (x-y))
    else:
        diag = y ** 2 - (y-1)
        print(diag - (-1)**y * (y-x))
    return


t = int(input())
while t > 0:
    sequence = list(map(int, input().split()))
    findNo(sequence[0], sequence[1])
    t -= 1
