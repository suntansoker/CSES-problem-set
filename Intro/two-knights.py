n = int(input())


def findPositions(sq):
    if sq == 1:
        return 0
    nos = sq * sq
    total = (nos * (nos-1)) // 2
    total -= 4 * (sq-1) * (sq-2)
    return total


for i in range(1, n+1):
    print(findPositions(i))
