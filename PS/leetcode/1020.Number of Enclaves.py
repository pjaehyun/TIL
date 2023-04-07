class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
                return
            grid[x][y] = 0
            dfs(x, y+1)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x-1, y)

        for i in range(m):
            dfs(0, i)
            dfs(n-1, i)
        
        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)
        
        answer = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 1:
                    answer += 1
        return answer
