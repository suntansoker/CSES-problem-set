n = int(input())


if n % 4==0 or (n+1) % 4 == 0:
    sm = (n * (n+1)) // 2
    print("YES")
    target = sm // 2
    # print(target)
    s1 = set()
    s2 = set()
    for i in range(1,n+1):
        s1.add(i)
    t = n
    
    while target-t>0:
        # print(s1)
        s1.remove(t)
        s2.add(t)
        if target-t<=0:
            break
        target -= t
        t -= 1

    if target in s1:
        s1.remove(target)
        s2.add(target)
    
    # print(s1)
    # print(s2)



    print(len(s1))
    str1 = ''
    for i in s1:
        str1 += str(i) + ' '
    print(str1)
    print(len(s2))
    str2 = ''
    for i in s2:
        str2 += str(i) + ' '
    print(str2)

else:
    print("NO")