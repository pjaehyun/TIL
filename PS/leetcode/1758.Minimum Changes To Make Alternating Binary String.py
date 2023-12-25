class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        op=[0]*2
    
        for i in range(0, n, 2):
            op[ord(s[i])&1]+=1
            if i+1<n:
                op[1-(ord(s[i+1])&1)]+=1
        return min(op[0], op[1])     