n, m = map(int, input().split())
arr = list(int(y) for y in input().split())


numbers = sorted([list(x) for x in enumerate(arr, start=1)], key=lambda x: x[1])

ans = 1

for i in range(1,n):
    if numbers[i][0] < numbers[i-1][0]:
        ans += 1

# print(numbers)

for i in range(m):
    i, j = map(int, input().split())

    f, s = arr[i-1], arr[j-1]
    idx1, idx2 = f-1, s-1
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    val1 = numbers[idx1][0]
    val2 = numbers[idx2][0]

    # print(idx1, idx2)
    # print(val1, val2)

    if idx2 == idx1 + 1:
        if val1>val2:
            ans -= 1
            # print("Here0:", ans)
        else:
            ans += 1
            # print("Here1:", ans)
    if idx1-1>=0:
        if numbers[idx1-1][0] > val1:
            ans -= 1
            # print("Here2:", ans)
        if numbers[idx1-1][0] > val2:
            ans += 1
            # print("Here3:", ans)
    if idx2+1<n:
        if val2 > numbers[idx2+1][0]:
            ans -= 1
            # print("Here4:", ans)
        if val1 > numbers[idx2+1][0]:
            ans += 1
            # print("Here5:", ans)
    if idx2 != idx1 + 1 and idx1+1<n:
        if val1 > numbers[idx1+1][0]:
            ans -= 1
            # print("Here6:", ans)
        if val2 > numbers[idx1+1][0]:
            ans += 1
            # print("Here7:", ans)
    if idx2 != idx1 + 1 and idx2-1>=0:
        if numbers[idx2-1][0] > val2:
            ans -= 1
            # print("Here8:", ans)
        if numbers[idx2-1][0] > val1:
            ans += 1
            # print("Here9:", ans)

    numbers[idx1][0], numbers[idx2][0] = numbers[idx2][0], numbers[idx1][0]
    
    print(ans)
    
    