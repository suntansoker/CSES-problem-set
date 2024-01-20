def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    newArr = sorted([(x, idx) for idx, x in enumerate(arr)])
    # print(newArr)

    # print(len(newArr))
    for i in range(n-2):
        sm = x - newArr[i][0]
        j, k = i+1, n-1
        while j<k:
            # print("j,k:", j, k)
            if newArr[j][0] + newArr[k][0] == sm:
                print(' '.join(str(x) for x in [newArr[i][1]+1,newArr[j][1]+1,newArr[k][1]+1]))
                return
            elif newArr[j][0] + newArr[k][0] < sm:
                j += 1
            else:
                k -= 1

    print("IMPOSSIBLE")

    return

if __name__=='__main__':
    main()


