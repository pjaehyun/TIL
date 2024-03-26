class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        
        positive = 1

        for i in range(len(nums)):
            if nums[i] == positive:
                positive += 1
        return positive