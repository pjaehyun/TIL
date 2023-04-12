class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0][0] = nums[0]
        answer = nums[0]

        for i in range(1, n):
            dp[i][0] = max(nums[i], dp[i-1][0] * nums[i], dp[i-1][1] * nums[i])
            dp[i][1] = min(nums[i], dp[i-1][1] * nums[i], dp[i-1][0] * nums[i])

            answer = max(answer, dp[i][0], dp[i][1])
        
        return answer