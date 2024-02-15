class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
        
        answer = -1

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] < nums[i-1]:
                answer = max(answer, nums[i])
        return answer