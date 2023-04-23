# 다른 해답 참고하여 풀이
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        
        n = len(s)
        dp = [0] * (n+1)
        dp[-1] = 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue
            j = i
            num = 0
            while j < n and int(s[i:j+1]) <= k:
                num += dp[j+1]
                j += 1
            dp[i] = num % (10**9+7)
        return dp[0]