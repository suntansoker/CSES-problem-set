def printNos(r):
    for i in range(2, r+1, 2):
        print(i, end=' ')
    for i in range(1, r+1, 2):
        print(i, end=' ')


ra = int(input())
if ra == 1:
    print(1)

elif ra == 2 or ra == 3:
    print("NO SOLUTION")

else:
    printNos(ra)
