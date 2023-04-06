# 첫번째 코드
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        if n <= 2 or m <= 2:
            return 0

        def dfs(x, y):
            for xx, yy in [(x, y+1),(x+1, y),(x, y-1),(x-1, y)]:
                if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] == 0:
                    grid[xx][yy] = 1
                    dfs(xx, yy)
        
        for i in range(m):
            if grid[0][i] == 0:
                grid[0][i] = 1
                dfs(0, i)
            if grid[n-1][i] == 0:
                grid[n-1][i] = 1
                dfs(n-1, i)
        
        for i in range(1, n-1):
            if grid[i][0] == 0:
                grid[i][0] = 1
                dfs(i, 0)
            if grid[i][m-1] == 0:
                grid[i][m-1] = 1
                dfs(i, m-1)
        count = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                    dfs(i, j)
                    count += 1
        return count

# 두번째 코드
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        if n <= 2 or m <= 2:
            return 0

        def dfs(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] != 0:
                return
            grid[x][y] = 1
            for xx, yy in [(x, y+1),(x+1, y),(x, y-1),(x-1, y)]:
                dfs(xx, yy)
        
        for i in range(m):
            dfs(0, i)
            dfs(n-1, i)
        
        for i in range(1, n-1):
                dfs(i, 0)
                dfs(i, m-1)
        count = 0
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0:
                    dfs(i, j)
                    count += 1
        return count