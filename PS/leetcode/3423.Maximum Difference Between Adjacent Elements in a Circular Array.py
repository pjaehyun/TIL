class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        
        answer = 0
        for i in range(n):
            answer = max(answer, abs(nums[i] - nums[(i+1)%n]))
        return answer