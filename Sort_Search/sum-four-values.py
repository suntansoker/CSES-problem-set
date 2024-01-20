from collections import defaultdict
def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    mp = defaultdict(list)

    for i in range(n-1):
        for j in range(i+1, n):
            if x - arr[i] - arr[j] in mp:
                print(str(i+1) + ' ' + str(j+1) + ' ' + str(mp[x - arr[i] - arr[j]][0] + 1)+ ' ' + str(mp[x - arr[i] - arr[j]][1] + 1))
                return
        for j in range(i):
            # Looping all the indices before the current i, j to put different indices visited into the map, to not getting duplication of indices in case of match
            mp[arr[i]+arr[j]] = [i, j]

    print("IMPOSSIBLE")

    return

if __name__=='__main__':
    main()