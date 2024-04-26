class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[float('inf')] * (m+2) for _ in range(n+2)]
        
        for i in range(1, m+1):
            dp[1][i] = grid[0][i-1]

        for i in range(2, n+1):
            for j in range(1, m+1):
                for k in range(1, m+1):
                    if k == j: continue
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + grid[i-1][j-1])
        return min(dp[n])