a, b = input().split()

n1 = len(a)
n2 = len(b)
a = '0' * (n2-n1) + a 

dp = {}

def findNos(idx, tightLow, tightHigh, prev, leadingZeroes):
    if idx == n2:
        return 1
    l, h = 0, 9

    if (idx, tightLow, tightHigh, prev, leadingZeroes) in dp:
        return dp[(idx, tightLow, tightHigh, prev, leadingZeroes)]

    if tightLow:
        l = int(a[idx])
    
    if tightHigh:
        h = int(b[idx])

    count = 0
    for i in range(l, h+1):
        if leadingZeroes==1 or i != prev:
            if i==0:
                count += findNos(idx+1, tightLow and i==int(a[idx]), tightHigh and i==int(b[idx]), i, leadingZeroes==1)
            else:
                 count += findNos(idx+1, tightLow and i==int(a[idx]), tightHigh and i==int(b[idx]), i, 0)
            

    dp[(idx, tightLow, tightHigh, prev, leadingZeroes)] = count

    return dp[(idx, tightLow, tightHigh, prev, leadingZeroes)]

# idx, tightLow, tightHigh, prev, leadingZeroes
print(findNos(0, 1, 1, -1, 1))