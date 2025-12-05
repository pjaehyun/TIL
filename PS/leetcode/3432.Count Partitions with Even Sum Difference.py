class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(1, n):
            nums[i] += nums[i-1]
        answer = 0
        for i in range(n-1):
            if (nums[i] - (nums[-1] - nums[i])) % 2 == 0:
                answer += 1
        return answer