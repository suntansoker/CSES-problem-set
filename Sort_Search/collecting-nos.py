n = int(input())
arr = list(int(y) for y in input().split())

numbers = sorted(list(enumerate(arr, start=1)), key=lambda x: x[1])

count = 1

for i in range(1,n):
    if numbers[i][0] < numbers[i-1][0]:
        count += 1

print(count)