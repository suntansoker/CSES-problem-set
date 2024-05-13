class manacher_algo:
    def __init__(self, s):
        self.st = s
        self.p = [1] * (2*len(s)+1)
        self.s = ""
        for st in s:
            self.s += "#" + st
        self.s += '#'
        
    def run_manacher(self):
        l, r = 1, 1
        n = len(self.s)

        for i in range(1, n):
            self.p[i] = max(0, min(r-i, self.p[l+r-i]))
            while((i + self.p[i])<n and (i-self.p[i])>=0 and self.s[i+self.p[i]]==self.s[i-self.p[i]]):
                self.p[i] += 1
            if (i+self.p[i]) > r:
                l = i-self.p[i]
                r = i+self.p[i]
    
    def longest_by_index(self, centre, odd):
        pos = 2*centre+1
        if not odd:
            pos += 1
        return self.p[pos] - 1

    def check_palindrome(l, r):
        if (r-l+1)<=longest_by_index((l+r) // 2, l%2==r%2):
            return 1
        return 0

    def longest_palindrome(self):
        idx, l = 0, 0
        for i in range(1, len(self.p)):
            if self.p[i]>l:
                idx = i
                l = self.p[i]

        actualIdx = 0
        st = ""
        if self.s[idx] == '#':
            if self.p[idx] == 1:
                return ""
            else:
                actualIdx = idx//2
                st = self.st[actualIdx - l//2:actualIdx]+self.st[actualIdx:actualIdx+l//2]
        else:
            actualIdx = idx // 2
            leftLength, rightLength = (l-1)//2, (l-1)//2

            st = self.st[actualIdx - leftLength:actualIdx]+ self.st[actualIdx] + self.st[actualIdx+1: actualIdx+1+rightLength]

        return st
        
# s = "babbabbabc"
# obj = manacher_algo(s)
# obj.run_manacher()
# st = obj.longest_palindrome()

s = input()
obj = manacher_algo(s)
obj.run_manacher()
st = obj.longest_palindrome()
print(st)