import heapq

n = int(input())
arr = [list(int(y) for y in input().split()) + [i] for i in range(n)]

roomId = 1
mxRoom = 0
pq = []
ans = [0] * n

arr.sort()

for a in arr:
    if len(pq) == 0 or pq[0][0]>=a[0]:
        heapq.heappush(pq, (a[1], a[0], a[2], roomId))
        mxRoom = max(roomId, mxRoom)
        roomId += 1
    else:
        endTime, startTime, index, roomNo = heapq.heappop(pq)
        ans[index] = roomNo
        heapq.heappush(pq, (a[1], a[0], a[2], roomNo))
        mxRoom = max(roomNo, mxRoom)

while pq:
    endTime, startTime, index, roomNo = heapq.heappop(pq)
    ans[index] = roomNo


print(mxRoom)
print(' '.join([str(x) for x in ans]))
