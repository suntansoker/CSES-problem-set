from collections import defaultdict

n, k = map(int,input().split())
arr = list(map(int, input().split()))

# with open('test_input.txt', 'r') as file:
#     n, k = map(int,file.readline().split())
#     arr = list(map(int, file.readline().split()))

mp = defaultdict(int)
count = 0

i, j = 0, 0

while j<n:
    mp[arr[j]] += 1
    while len(mp)>k and i<j:
        mp[arr[i]] -= 1
        if mp[arr[i]] == 0:
            del mp[arr[i]]
        i += 1
    count += j-i+1
    j += 1

print(count)

