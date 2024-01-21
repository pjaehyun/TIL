# 첫번째 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = nums[0], nums[1]

        for i in range(3, n+1):
            dp[i] = max(nums[i-1] + dp[i-2], nums[i-1] + dp[i-3])
        return max(dp)
    
# 두번째 풀이
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp = [0] * (n + 1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])
        return max(dp[-1], dp[-2])