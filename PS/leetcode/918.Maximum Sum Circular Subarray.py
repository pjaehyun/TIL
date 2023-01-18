# 첫번째 풀이
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        answer = nums[0]

        dp = [[0,0] for _ in range(n)]
        dp[0][0] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(nums[i], nums[i] + dp[i-1][0]) # max subarray
            dp[i][1] = min(nums[i], nums[i] + dp[i-1][1]) # min subarray

            # cur value, max subarray, total - min subarray
            answer = max(answer, dp[i][0], total - dp[i][1])
        return answer

# 두번째 풀이         
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        answer = nums[0]

        min_value = 0
        max_value = nums[0]

        for i in range(1, n):
            max_value = max(nums[i], nums[i] + max_value) # max subarray
            min_value = min(nums[i], nums[i] + min_value) # min subarray

            # cur value, max subarray, total - min subarray
            answer = max(answer, max_value, total - min_value)
        return answer

