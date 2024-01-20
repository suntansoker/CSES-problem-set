from collections import defaultdict
n = int(input())
arr = list(map(int, input().split()))

# with open('test_input.txt', 'r') as file:
#     n = map(int,file.readline())
#     arr = list(map(int, file.readline().split()))

mp = defaultdict(int)

mp[0] = 1
ans = 0
sm = 0

for a in arr:
    sm += a
    ans += mp[(sm + n) % n]
    mp[(sm+n) % n] += 1

print(ans)