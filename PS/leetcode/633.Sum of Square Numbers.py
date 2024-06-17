class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        for i in range(int(sqrt(c)) + 1):
            temp = i**2
            if int(sqrt(c - temp))**2 == c - temp:
                return True
        return False