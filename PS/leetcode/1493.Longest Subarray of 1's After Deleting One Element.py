class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        zero = 1
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zero -= 1
            
            if zero < 0:
                if nums[l] == 0:
                    zero += 1
                l += 1
        return r - l