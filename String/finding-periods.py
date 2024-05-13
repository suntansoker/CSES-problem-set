def findZArray(s, n):
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

text = input()
n = len(text)

zArr = findZArray(text, n)
ans = []

for i in range(n):
    if zArr[i] + i == n:
        ans.append(i)

ans.append(n)

print(" ".join(str(x) for x in ans))