class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        def recursion(l, r):
            if dp[l][r] != -1:
                return dp[l][r]
            
            if l == r:
                return nums[l]
            
            left = nums[l] - recursion(l+1, r)
            right = nums[r] - recursion(l, r-1)
            dp[l][r] = max(left, right)
        
            return dp[l][r]

        n = len(nums)
        dp = [[-1] * n for _ in range(n)]
        return recursion(0, n - 1) >= 0