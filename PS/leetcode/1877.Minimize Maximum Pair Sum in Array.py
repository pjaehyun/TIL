class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        min_max_sum = 0
        for i in range(len(nums) // 2):
            min_max_sum = max(min_max_sum, nums[i] + nums[len(nums) - 1 - i])
            
        return min_max_sum