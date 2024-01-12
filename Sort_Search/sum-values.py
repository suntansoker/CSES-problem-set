n, x = map(int, input().split())
arr = list(int(y) for y in input().split())

indexed_numbers = sorted(list(enumerate(arr, start=1)), key=lambda x: x[1])

i, j = 0, n-1
output = []

while i<j:
    if indexed_numbers[i][1] + indexed_numbers[j][1] == x:
        output = [indexed_numbers[i][0], indexed_numbers[j][0]]
        break
    elif indexed_numbers[i][1] + indexed_numbers[j][1] < x:
        i += 1
    else:
        j -= 1

if len(output) > 0:
    output = ' '.join(str(x) for x in [indexed_numbers[i][0], indexed_numbers[j][0]])
    print(output)
else:
    print("IMPOSSIBLE")
