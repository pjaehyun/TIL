class Solution:
    def countSquares(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    dp[i + 1][j + 1] = 1 + min(dp[i][j], dp[i + 1][j], dp[i][j + 1])
                    ans += dp[i + 1][j + 1]
        
        return ans