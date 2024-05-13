class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        node = self.root
        n = len(word)
        for i in range(n):
            idx = ord(word[i]) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.isEnd
    
    def insert(self, word):
        node = self.root
        n = len(word)
        for i in range(n):
            idx = ord(word[i]) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.isEnd = True

w = input()
n = int(input())
words = [input() for x in range(n)]

obj = Trie()
for word in words:
    obj.insert(word)

l = len(w)
dp = [0] * (l+1)

dp[l] = 1

MOD = 1000000007

for i in range(l-1, -1 , -1):
    test = obj.root
    for j in range(i, l):
        idx = ord(w[j]) - ord('a')
        if not test.children[idx]:
            break
        test = test.children[idx]
        if test.isEnd:
            dp[i] = (dp[i] + dp[j+1]) % MOD

print(dp[0] % MOD)