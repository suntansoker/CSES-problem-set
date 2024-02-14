n, q = map(int, input().split())
arr = [int(x) for x in input().split()]

queries = [[int(x) for x in input().split()] for _ in range(q)]

prefix = [0] * (n+1)

for i in range(1, n+1):
    prefix[i] = prefix[i-1] + arr[i-1]

for q1, q2 in queries:
    print(prefix[q2] - prefix[q1-1])