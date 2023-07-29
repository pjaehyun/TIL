class Solution:
    def soupServings(self, n: int) -> float:
        A = [100, 75, 50, 25]
        B = [0, 25, 50, 75]

        def dfs(a, b):
            if a == 0 and b == 0:
                return 0.5
            if a == 0:
                return 1
            if b == 0:
                return 0

            if dp[a][b] != -1:
                return dp[a][b]
            
            res = 0
            for i in range(4):
                aa = a - A[i]
                bb = b - B[i]
                res += 0.25 * dfs(max(aa, 0), max(bb, 0))
            dp[a][b] = res
            return res
        if n >= 4800:
            return 1
        dp = [[-1] * (n+1) for _ in range(n+1)]
        return dfs(n, n)