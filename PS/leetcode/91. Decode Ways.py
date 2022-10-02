class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s) + 1)]
        dp[0], dp[1] = 1, 1

        if s[0] == '0' or len(s) <= 0: return 0

        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i + 1] = dp[i + 1] + dp[i]
            if s[i - 1] != '0' and 1 <= int(s[i-1:i+1]) <= 26:
                dp[i + 1] = dp[i + 1] + dp[i - 1]
        return dp[len(s)]