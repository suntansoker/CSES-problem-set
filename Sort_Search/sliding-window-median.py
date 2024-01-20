# WITH SORTEDLIST

# from sortedcontainers import SortedList

# n, k = map(int, input().split())
# arr = list(map(int, input().split()))

# lst = SortedList()
# lst = []
# odd = False
# ans = []

# if k%2 == 1:
#     odd = True
# for i in range(n):
#     lst.add((arr[i], i))
#     lst.sort()
#     if i >= k-1:
#         if i != k-1:
#             lst.remove((arr[i-k], i-k))
#         if odd:
#             ans.append(lst[(k-1)//2][0])
#         else:
#             ans.append((lst[(k-1)//2][0] + lst[k//2][0]) / 2)

# print(' '.join(str(x) for x in ans))

# WITHOUT SORTEDLIST

n, k = map(int, input().split())
arr = list(map(int, input().split()))

lst = []
odd = False
ans = []

if k%2 == 1:
    odd = True
for i in range(n):
    # lst.add((arr[i], i))
    lst.append((arr[i], i))
    lst.sort()
    if i >= k-1:
        if i != k-1:
            # lst.remove((arr[i-k], i-k))
            lst.pop(lst.index((arr[i-k], i-k)))
        if odd:
            ans.append(lst[(k-1)//2][0])
        else:
            # ans.append((lst[(k-1)//2][0] + lst[k//2][0]) / 2)
            ans.append(lst[(k-1)//2][0])

print(' '.join(str(x) for x in ans))