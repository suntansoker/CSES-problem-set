import math
from collections import defaultdict
import sys

sys.setrecursionlimit(1<<30)

n = int(input())
colors = [{x} for x in input().split()]
edges = [[int(x)-1 for x in input().split()] for _ in range(n-1)]

adj = defaultdict(list)

for e1, e2 in edges:
    adj[e1].append(e2)
    adj[e2].append(e1)

count = [0] * n

def findColors(node, parent):
    for it in adj[node]:
        if it != parent:
            findColors(it, node)
            if len(colors[node]) < len(colors[it]):
                colors[node], colors[it] = colors[it], colors[node]

            for color in list(colors[it]):
                colors[node].add(color)

    count[node] = len(colors[node])

findColors(0, -1)

print(" ".join(str(x) for x in count))

