class Solution:
    def countOrders(self, n: int) -> int:
        mod = (10**9) + 7

        dp = [0] * (n+1)

        dp[0] = 1

        for curr in range(1, n+1):
            dp[curr] = dp[curr-1] * (2 * curr - 1) * curr % mod
        return dp[-1]