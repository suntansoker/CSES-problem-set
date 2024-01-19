from collections import Counter

def solve():
    x, n = map(int, input().split())
    arr = list(int(y) for y in input().split())
    position = {0, x}
    length = Counter([x]) # constructs {x:1}

    for a in arr:
        no = a
        position.add(no)
        it = sorted(position).index(no)
        
        previous_val = sorted(position)[it - 1]
        next_val = sorted(position)[it + 1]
        
        length[next_val - previous_val] -= 1
        if length[next_val - previous_val] == 0:
            del length[next_val - previous_val]
        
        length[no - previous_val] += 1
        length[next_val - no] += 1
        
        print(max(length.elements()), end=" ")

if __name__ == "__main__":
    solve()
