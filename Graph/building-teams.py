from collections import defaultdict

def main():
    n, m = map(int, input().split())
    arr = [[int(x) for x in input().split()] for _ in range(m)]

    adj = defaultdict(list)
    for a1, a2 in arr:
        adj[a1].append(a2)
        adj[a2].append(a1)

    color = [-1] * (n+1)

    def isBipartite(node, color):
        stack = [(node, 1)]

        while stack:
            current, current_color = stack.pop()

            if color[current] == -1:
                color[current] = current_color

            for neighbor in adj[current]:
                if color[neighbor] == -1:
                    color[neighbor] = 3 - current_color
                    stack.append((neighbor, 3 - current_color))
                elif color[neighbor] == color[current]:
                    return False

        return True

    for i in range(1, n+1):
        if not isBipartite(i, color):
            print("IMPOSSIBLE")
            return

    print(' '.join([str(x) for x in color[1:]]))



if __name__=='__main__':
    main()