n, k = map(int, input().split())
arr = list(map(int, input().split()))

# with open('test_input.txt', 'r') as file:
#     n, k = map(int,file.readline().split())
#     arr = list(map(int, file.readline().split()))

ans = 0
left, right = max(arr), 10 ** 18

def good(mid):
    grps = 0
    sm = 0
    for a in arr:
        if sm + a > mid:
            grps += 1
            sm = a
        else:
            sm += a

    if sm>0:
        grps +=1

    if grps <= k:
        return True
    
    return False

while(left<=right):
    mid = (left + right) // 2
    if good(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)



