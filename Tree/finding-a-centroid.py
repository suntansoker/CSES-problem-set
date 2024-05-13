import math
from collections import defaultdict
import sys

sys.setrecursionlimit(1<<30)

n = int(input())
edges = [[int(x) for x in input().split()] for _ in range(n-1)]
size = [0] * (n+1)

adj = defaultdict(list)

for e1, e2 in edges:
    adj[e1].append(e2)
    adj[e2].append(e1)

def findSubtreeSize(node, parent):
    size[node] = 1
    for it in adj[node]:
        if it == parent:
            continue
        findSubtreeSize(it, node)
        size[node] += size[it]

def findCentroid(node, parent):
    possibleNode, mx = 0, 0

    for it in adj[node]:
        if it == parent:
            continue
        if size[it] > mx:
            possibleNode = it
            mx = size[it]

    if mx<=n//2:
        return node
    else:
        return findCentroid(possibleNode, node)

findSubtreeSize(1, 0)

print(findCentroid(1, 0))

