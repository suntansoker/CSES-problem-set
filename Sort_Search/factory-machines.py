n, t = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 1, 10 ** 18

def good(mid):
    res = 0
    possible = False
    for a in arr:
        res += mid // a
        if res>=t:
            possible=True
            break

    if possible:
        return True

    return False

ans = 0
while left<=right:
    mid = (left + right) // 2
    if good(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)
