class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9+7

        def dfs(i, j, step):
            if step < 0:
                return 0
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            
            if (i, j, step) in dp:
                return dp[(i, j, step)]
            
            res = 0
            for ni, nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                res += dfs(ni, nj, step - 1)
            
            dp[(i, j, step)] = res % MOD

            return dp[(i, j, step)]
        
        dp = {}
        return dfs(startRow, startColumn, maxMove)

