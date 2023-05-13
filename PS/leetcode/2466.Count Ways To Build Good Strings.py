class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high+1)

        dp[0] = 1
        mod = 10**9+7
        for i in range(1, high+1):
            if i >= zero:
                dp[i] = (dp[i] + dp[i-zero]) % mod

            if i >= one:
                dp[i] = (dp[i] + dp[i-one]) % mod
        return sum(dp[x] for x in range(low, high+1))