n = int(input())

def getCodes(n):
    cur = []
    if n==1:
        cur.append('0')
        cur.append('1')
        return cur
    prev = getCodes(n-1)
    for i in range(len(prev)):
        cur.append('0'+prev[i])
    for i in range(len(prev)-1, -1, -1):
        cur.append('1' + prev[i])

    return cur

arr = getCodes(n)

for a in arr:
    print(a)