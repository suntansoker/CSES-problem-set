n, k = map(int, input().split())

children = SortedList(range(1, n + 1))

index = k + 1
while len(children) > 1:
    index %= len(children)
    if index == 0:
        index = len(children)

    current_child = children[index - 1]
    print(current_child, end=" ")
    children.remove(current_child)

    index += k

print(children[0])