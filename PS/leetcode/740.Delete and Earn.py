class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        n = max(nums)
        dp = [0] * (n+1)
        for x in nums:
            dp[x] += x
        for i in range(2, n+1):
            dp[i] = max(dp[i-2] + dp[i], dp[i-1])
        return dp[-1]