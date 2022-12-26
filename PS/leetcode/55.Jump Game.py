class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        i, j = len(nums) - 1, len(nums) - 2
        while j >= 0:
            if j + nums[j] >= i:
                i = j
                j -= 1
            else:
                j -= 1
        
        return True if i <= 0 else False