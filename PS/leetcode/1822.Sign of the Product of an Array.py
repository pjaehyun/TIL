class Solution:
    def arraySign(self, nums: List[int]) -> int:
        nums.sort()

        negative = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            
            if nums[i] < 0:
                negative += 1
        if negative % 2 == 0:
            return 1
        return -1