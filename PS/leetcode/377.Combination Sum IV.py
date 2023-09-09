class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (target+1)

        def dfs(n, nums, target, dp):
            if target == 0:
                return 1
            if target < 0:
                return 0
            
            if dp[target] != -1:
                return dp[target]
            
            take = 0
            for j in range(n):
                take += dfs(n, nums, target - nums[j], dp)
            
            dp[target] = take
            return take
        return dfs(len(nums), nums, target, dp)