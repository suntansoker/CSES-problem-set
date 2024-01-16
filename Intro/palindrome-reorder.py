st = input()

n = len(st)
arr = [0] * 26
res = [''] * n

for i in st:
    arr[ord(i) - ord('A')] += 1

count_odd = 0
idx = -1

for i in range(26):
    if arr[i] % 2 == 1:
        count_odd += 1
        idx = i


if count_odd > 1 or (n%2==0 and count_odd >= 1):
    print("NO SOLUTION")
else:
    i, j = 0, n-1
    for a in range(26):
        if arr[a]>0 and arr[a] % 2 == 0:
            for k in range(0,arr[a], 2):
                ch = chr(ord('A') + a)
                res[i] = ch
                i += 1
                res[j] = ch
                j -= 1
    if n % 2 == 1:
        m = n//2 - arr[idx]//2
        # print(m)
        while arr[idx]>0:
            res[m] = chr(ord('A')+ idx)
            arr[idx] -= 1
            m += 1

    print(''.join(res))




