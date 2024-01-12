n = int(input())
arr = [int(y) for y in input().split()]
st = set()
ans = 0

i, j = 0, 0

for i in range(n):
    while arr[i] in st:
        st.remove(arr[j])
        j += 1
    st.add(arr[i])
    ans = max(ans, len(st))
    i += 1

print(ans)


