class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        temp = original

        while temp in nums:
            temp *= 2
        return temp