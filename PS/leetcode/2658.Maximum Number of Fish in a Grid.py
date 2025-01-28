class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, dir = len(grid), len(grid[0]), [-1,0,1,0,-1]
        
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            for k in range(4):
                res += dfs(i+dir[k], j+dir[k+1])
            return res
        
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    max_fish = max(max_fish, dfs(i,j))
        return max_fish