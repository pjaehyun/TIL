class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (1001)
        dp[1], dp[2], dp[3] = 1, 2, 5

        if n <= 3:
            return dp[n]

        for i in range(4, n+1):
            dp[i] = dp[i-1] * 2 + dp[i-3]
        return dp[n] % (10**9 + 7)