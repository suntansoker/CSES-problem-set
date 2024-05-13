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

def kmp_search(text, pattern):
    """
    Search for occurrences of the pattern in the text using the KMP algorithm.
    Return the count of occurrences.
    """
    count = 0
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == m:
                count += 1
                j = lps[j - 1]
    return count

# Example usage:
text = input()
pattern = input()
print(kmp_search(text, pattern))