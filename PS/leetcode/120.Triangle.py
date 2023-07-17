class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float('inf')] * (len(triangle[i]) + 2) for i in range(len(triangle))]
        
        dp[0][1] = triangle[0][0]
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j-1]
        return min(dp[-1])
