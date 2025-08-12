class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        from functools import lru_cache
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(remaining, current):
            if remaining == 0:
                return 1
            if remaining < 0 or current ** x > remaining:
                return 0

            power = current ** x
            include = dp(remaining - power, current + 1)
            skip = dp(remaining, current + 1)
            return (include + skip) % MOD

        return dp(n, 1)