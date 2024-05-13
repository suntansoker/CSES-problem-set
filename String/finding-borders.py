def compute_lps_array(pattern):
    """
    Compute the Longest Prefix Suffix (LPS) array for the given pattern.
    """
    length = len(pattern)
    lps = [0] * length
    j = 0
    for i in range(1, length):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        lps[i] = j
    return lps

text = input()
lps = compute_lps_array(text)

arr = []
j = lps[-1]

while j>0:
    arr.append(j)
    j = lps[j-1]

arr.sort()

print(" ".join(str(x) for x in arr))