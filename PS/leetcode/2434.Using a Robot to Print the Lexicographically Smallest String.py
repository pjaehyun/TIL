class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        s = list(s)        
        t = []
        p = []
        suffixMin = [''] * n
        suffixMin[n - 1] = s[n - 1]
        
        for i in range(n - 2, -1, -1):
            if s[i] < suffixMin[i + 1]:
                suffixMin[i] = s[i]
            else:
                suffixMin[i] = suffixMin[i + 1]
                
        i = 0
        while i < n:
            if s[i] == suffixMin[i]:
                p.append(s[i])
                i += 1
                while t and (i == n or t[-1] <= suffixMin[i]):
                    p.append(t.pop())
                    
            else:
                t.append(s[i])
                i += 1
                
        while t:
            p.append(t.pop())
            
        return "".join(p)        