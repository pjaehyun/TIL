class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[0] * m for _ in range(m)] for _ in range(n)]

        cherries = 0
        dp[0][0][m - 1] = grid[0][0] + grid[0][m - 1]

        for i in range(1, n):
            for j in range(m):
                for k in range(m):
                    if j > i or k < m - i - 1 or j > k:
                        continue
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k])
                    if j - 1 >= 0 and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1])
                    if j - 1 >= 0 and k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k + 1])
                    if j + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k])
                    if j + 1 < m and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k - 1])
                    if j + 1 < m and k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k + 1])
                    if k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                    if k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k + 1])
                    if j != k:
                        dp[i][j][k] += grid[i][j] + grid[i][k]
                    else:
                        dp[i][j][k] += grid[i][j]
                    cherries = max(cherries, dp[i][j][k])

        return cherries