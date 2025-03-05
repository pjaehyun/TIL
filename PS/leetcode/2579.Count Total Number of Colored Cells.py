class Solution:
    def coloredCells(self, n: int) -> int:
        
        res = 1

        for i in range(1, n):
            res = (res + i*4)
        return res