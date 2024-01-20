n = int(input())
arr = list(map(int, input().split()))

res = [0] * n

q = []

for i in range(len(arr)):
    while len(q) > 0 and q[-1][0] >= arr[i]:
        q.pop()

    if len(q) == 0:
        res[i] = 0
    else:
        res[i] = q[-1][1]
    
    q.append((arr[i], i+1))

print(' '.join(str(x) for x in res))

    


    