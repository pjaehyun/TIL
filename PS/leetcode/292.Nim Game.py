class Solution:
    def canWinNim(self, n: int) -> bool:
        
        if n%4 == 0:
            return False
        
        return True