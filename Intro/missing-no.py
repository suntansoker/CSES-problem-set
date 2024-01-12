def find_missing(n, sequence):
    ans = 0
    count = 1
    while count<n:
        ans ^= sequence[count-1] ^ count
        count += 1

    print(ans^n)
    return
n = int(input())
sequence = list(map(int, input().split()))

find_missing(n, sequence)