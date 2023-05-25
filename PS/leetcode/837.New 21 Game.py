class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k+maxPts:
            return 1.0
        
        dp = [0] * (n+1)
        dp[0] = 1.0

        sliding = 1.0
        for i in range(1, n+1):
            dp[i] = sliding / maxPts
            if i < k:
                sliding += dp[i]
            if i >= maxPts:
                sliding -= dp[i-maxPts]
        return sum(dp[k:])