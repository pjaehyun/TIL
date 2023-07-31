# 첫번째 풀이(다른 풀이 참고)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [0] * (len(s2) + 1)
        for i in range(1, len(s2) + 1):
            dp[i] = dp[i-1] + ord(s2[i-1])
        
        for i in range(1, len(s1) + 1):
            curr = [dp[0] + ord(s1[i-1])]
            for j in range(1, len(s2) + 1):
                if s1[i-1] == s2[j-1]:
                    curr.append(dp[j-1])
                else:
                    curr.append(min(dp[j] + ord(s1[i-1]), curr[j-1] + ord(s2[j-1])))
            dp = curr
        return dp[-1]
    
# 두번째 풀이(기본적인 LCS 응용)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s2[j-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        comm = dp[-1][-1]
        return sum(ord(x) for x in s1+s2) - comm * 2