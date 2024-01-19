from sortedcontainers import SortedList
n, k = map(int, input().split())

children = SortedList(range(1, n + 1))
# children = [i for i in range(1, n+1)]

index = k
while len(children) > 1:
    index %= len(children)

    current_child = children[index]
    print(current_child, end=" ")
    children.remove(current_child)

    index += k

print(children[0])