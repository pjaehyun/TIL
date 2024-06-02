class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        n = len(s)
        n0 = n//2

        for i in range(n0):
            temp = s[i]
            s[i] = s[n-1-i]
            s[n-1-i] = temp