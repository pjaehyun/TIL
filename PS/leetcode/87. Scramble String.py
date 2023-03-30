# 문제 해결 못함, 정답보고 풀이

# DP
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        if n != len(s2):
            return False
        
        dp = [[[False for _ in range(n)]for _ in range(n)] for _ in range(n+1)]
        
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[1][i][j] = True
        
        for l in range(2, n+1):
            for i in range(n-l+1):
                for j in range(n-l+1):
                    for k in range(1, l):
                        if (dp[k][i][j] and dp[l-k][i+k][j+k] or dp[k][i][j+l-k] and dp[l-k][i+k][j]):
                            dp[l][i][j] = True
                            break
        return dp[n][0][0]

# DFS
class Solution:
    def __init__(self):
      self.scrambles = {}

    def isScramble(self, s1: str, s2: str) -> bool:
      if (s1, s2) in self.scrambles:
        return self.scrambles[(s1,s2)]
      
      if s1 == s2:
        self.scrambles[(s1,s2)] = True
        return True
      
      n = len(s1)
      if n == 1 or sorted(s1) != sorted(s2):
        self.scrambles[(s1,s2)] = False
        return False
      
      for i in range(1, n):
        same1 = self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])

        same2 = self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i])

        if same1 or same2:
          self.scrambles[(s1,s2)] = True
          return True
      self.scrambles[(s1, s2)] = False
      return False