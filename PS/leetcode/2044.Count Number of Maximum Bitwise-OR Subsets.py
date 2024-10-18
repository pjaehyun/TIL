from typing import List

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        def backtrack(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            include = backtrack(index + 1, current_or | nums[index])
            exclude = backtrack(index + 1, current_or)
            return include + exclude
        
        return backtrack(0, 0)