class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
               
                if i == j:
                    dp[i][j] = True
                elif j == i + 1:
                  
                    dp[i][j] = (s[i] == s[j])
                else:
                   
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

               
                if dp[i][j]:
                    count += 1

        return count
        