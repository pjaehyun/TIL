class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        n = len(piles)
        dp = [[0] * (k+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, k+1):
                cur = 0
                for x in range(min(len(piles[i-1]), j)):
                    cur += piles[i-1][x]
                    dp[i][j] = max(dp[i][j], cur + dp[i-1][j-x-1])
                dp[i][j] = max(dp[i][j], dp[i-1][j])
                
        return dp[n][k]