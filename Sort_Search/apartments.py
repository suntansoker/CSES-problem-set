n, m, k = map(int, input().split())
applicant_sizes = sorted(int(x) for x in input().split())
apartment_sizes = sorted(int(x) for x in input().split())


count = 0
i, j = 0, 0

while i < n and j < m:
    if abs(applicant_sizes[i] - apartment_sizes[j]) <= k:
        i += 1
        j += 1
        count += 1
    elif applicant_sizes[i] - k > apartment_sizes[j]:
        j += 1
    else:
        i += 1


print(count)
