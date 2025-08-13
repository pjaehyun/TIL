class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        pot = 1

        while pot <= n:
            if pot == n: return True
            pot = pot * 3
        return False
