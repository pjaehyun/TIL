class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1,x+1):
            if i*i==x:
                return i
            elif i*i>x:
                return i-1
        return 0 
