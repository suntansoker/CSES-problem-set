n = int(input())

arr = []

for i in range(n):
    arr.append(i+1)

while len(arr)>1:
    survivors = []
    for i in range(len(arr)):
        if i%2 == 1:
            print(arr[i], end= " ")
        else:
            survivors.append(arr[i])

    if len(arr) % 2==0:
        arr.clear()
        arr = survivors
    else:
        arr.clear()
        popped=survivors.pop()
        arr.append(popped)
        for a in survivors:
            arr.append(a)

print(arr[0])