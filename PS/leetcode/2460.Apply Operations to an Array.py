class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] = nums[i-1] * 2
                nums[i] = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], nums[i]
                        break

        return nums