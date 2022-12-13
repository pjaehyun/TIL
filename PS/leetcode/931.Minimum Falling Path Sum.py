class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        dp = [[inf] * (m+2) for _ in range(n)]
        for i in range(1, m+1):
            dp[0][i] = matrix[0][i-1]
        
        for i in range(1, n):
            for j in range(1, m+1):
                dp[i][j] = min(dp[i][j], matrix[i][j-1] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1]))
        return min(dp[-1])