class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])

        preSum = [[0] * (n+1) for _ in range(m+1)]
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                preSum[r][c] = preSum[r+1][c] + preSum[r][c+1] - preSum[r+1][c+1] + (pizza[r][c] == 'A')
        
        dp = [[[None] * n for _ in range(m)]for _ in range(k)]
        return self.dfs(m, n, 0, 0, k-1, dp, preSum)

        
    def dfs(self, m, n, r, c, k, dp, preSum):
        if preSum[r][c] == 0:
            return 0

        if k == 0:
            return 1

        if dp[k][r][c] is not None:
            return dp[k][r][c]
        
        answer = 0

        for rr in range(r+1, m):
            if preSum[r][c] > preSum[rr][c]:
                answer = (answer + self.dfs(m, n, rr, c, k-1, dp, preSum)) % 1000000007
        for cc in range(c+1, n):
            if preSum[r][c] > preSum[r][cc]:
                answer = (answer + self.dfs(m, n, r, cc, k-1, dp, preSum)) % 1000000007
        
        dp[k][r][c] = answer
        return answer
        