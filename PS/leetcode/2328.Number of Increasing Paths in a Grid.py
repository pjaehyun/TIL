class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(x, y):
            res = 1
            for xx, yy in [[x+1,y],[x,y-1],[x-1, y],[x, y+1]]:
                if 0 <= xx < n and 0 <= yy < m and grid[xx][yy] > grid[x][y]:
                    res += dfs(xx, yy)
            return res
                
        path_count = []
        for i in range(n):
            for j in range(m):
                path_count.append(dfs(i, j))
        return sum(path_count) % (10**9+7)