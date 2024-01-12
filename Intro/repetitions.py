def findLongest(seq):
    last = ''
    count = 0
    mx = 0

    for i in range(len(seq)):
        if last == seq[i]:
            count += 1
        else:
            count = 1
            last = seq[i]
        mx = max(mx, count)
    return mx


sequence = input()
m = findLongest(sequence)
print(m)
