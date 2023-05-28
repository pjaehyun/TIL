# 해결못해서 정답 봄😡
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = sorted([0] + cuts + [n])
        m = len(cuts)

        dp = [[0] * m for _ in range(m)]

        for l in range(2, m):
            for i in range(m - l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i+1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])
        return dp[0][m-1]