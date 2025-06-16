class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        answer = -1
        for i in range(n):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    answer = max(answer, nums[j] - nums[i])
        return answer