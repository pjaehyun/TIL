class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
            return "none"

        if nums[0] == nums[1] == nums[2]:
            return "equilateral"
        if nums[0] != nums[1] == nums[2] or nums[0] == nums[1] != nums[2] or nums[0] == nums[2] != nums[1]:
            return "isosceles"
        if nums[0] != nums[1] != nums[2]:
            return "scalene"