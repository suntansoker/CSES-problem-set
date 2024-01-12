def findMin(arr, n):
    last = arr[0]
    ans = 0

    for i in range(1, n):
        if last > arr[i]:
            ans += last - arr[i]
        else:
            last = arr[i]

    return ans


n = int(input())
arr = list(map(int, input().split()))
print(findMin(arr, n))
