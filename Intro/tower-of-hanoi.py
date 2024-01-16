n = int(input())

def findMoves(start, end, through, n):
    if n==0:
        return
    findMoves(start, through, end, n-1)
    st = str(start) + ' ' + str(end)
    print(st)
    findMoves(through, end, start, n-1)
    return

print(2 ** n -1)
findMoves(1, 3, 2, n)