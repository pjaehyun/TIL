class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = 0
        for i in range(1, len(nums)):
            if nums[result] != nums[i]:
                result += 1
                nums[result] = nums[i]

        return result + 1