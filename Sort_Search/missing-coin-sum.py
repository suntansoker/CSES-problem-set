n = int(input())
arr = sorted(int(y) for y in input().split())

rangeMax, outofRange = 0, -1
for i in range(n):
    if arr[i]<= rangeMax + 1:
        rangeMax = arr[i] + rangeMax
    else:
        outofRange = rangeMax + 1
        break

if outofRange == -1:
    outofRange = rangeMax + 1

print(outofRange)
