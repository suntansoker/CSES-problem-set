s = input()

# st = set()

# def findStrings(prefix, s):
#     n = len(s)
#     if n==0:
#         st.add(prefix)
#     for i in range(n):
#         findStrings(prefix + s[i], s[0:i]+s[i+1:n])

# findStrings('', s)
# print(len(st))
# for e in sorted(list(st)):
#     print(e)

from itertools import permutations
lst = sorted(list(set(permutations(s))))
print(len(lst))
for p in lst:
    print(''.join(p))
