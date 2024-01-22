n, a, b = map(int, input().split())
arr = list(int(y) for y in input().split())

# WITH SORTEDLIST
# from sortedcontainers import SortedList

# prefix = [0] * (n+1)
# for i in range(1, n+1):
#     prefix[i] = prefix[i-1] + arr[i-1]

# st = SortedList()
# mxSum = - (10 ** 18)

# for i in range(a, b+1):
#     st.add((prefix[i], i))

# for i in range(1, n-a+2):
#     mxElement = st[-1][0]
#     mxSum = max(mxSum, mxElement - prefix[i-1])
#     st.remove((prefix[i+a-1], i+a-1))
#     if i+b<=n:
#         st.add((prefix[i+b], i+b))
    

# print(mxSum)

# WITHOUT SORTEDLIST

prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

st = []
mxSum = - (10 ** 18)

for i in range(a, b+1):
    st.append((prefix[i], i))

st.sort()

for i in range(1, n-a+2):
    mxElement = st[-1][0]
    mxSum = max(mxSum, mxElement - prefix[i-1])
    st.remove((prefix[i+a-1], i+a-1))
    if i+b<=n:
        st.append((prefix[i+b], i+b))
    st.sort()
    

print(mxSum)



