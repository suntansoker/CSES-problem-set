import sys
from collections import defaultdict
sys.setrecursionlimit(1<<30)
n = int(input())
arr = [[int(x) for x in input().split()] for _ in range(n-1)]

subTreeAns = [0] * (n+1) #Gives the ans for a node with a subtree
subTreeNodes = [0] * (n+1) #Gives the no of nodes present in a subtree
adj = defaultdict(list)
ans = [0] * (n+1)

for e1, e2 in arr:
    adj[e1].append(e2)
    adj[e2].append(e1)

def findNodes(node, parent):
    noOfNodes = 1
    ansForNode = 0
    for it in adj[node]:
        if it != parent:
            findNodes(it, node)
            noOfNodes += subTreeNodes[it]
            ansForNode += subTreeAns[it] + subTreeNodes[it]

    subTreeNodes[node] = noOfNodes
    subTreeAns[node] = ansForNode

def findAns(node, parent, partial_ans):
    ans[node] = subTreeAns[node] + partial_ans + n - subTreeNodes[node]
    for it in adj[node]:
        if it != parent:
            findAns(it, node, ans[node] - subTreeAns[it] - subTreeNodes[it])

findNodes(1, 0)
findAns(1, 0, 0)

print(' '.join(str(x) for x in ans[1:]))

