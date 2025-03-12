class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        max_value = float('-inf')
        curr = 0
        for i in range(len(nums)):
            curr = max(0, curr + nums[i])
            max_value = max(max_value, curr)
        
        min_value = float('inf')
        curr = 0

        for i in range(len(nums)):
            curr = min(0, curr + nums[i])
            min_value = min(min_value, curr)
        return max(max_value, abs(min_value))