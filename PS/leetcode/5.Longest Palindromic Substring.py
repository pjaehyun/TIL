class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        answer = ''
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            answer = s[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if len(answer) < len(s[i:j+1]):
                            answer = s[i:j+1]
        return answer