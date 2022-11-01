class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        N, M = len(grid), len(grid[0])
        result = [0] * M
        def dfs(x, y):
            if x >= N:
                return y
            if grid[x][y] == 1:
                if y + 1 >= M:
                    return -1
                if grid[x][y + 1] == -1:
                    return -1
                return dfs(x + 1, y + 1)
            if grid[x][y] == -1:
                if y - 1 < 0:
                    return -1
                if grid[x][y - 1] == 1:
                    return -1
                return dfs(x + 1, y - 1)
        for i in range(M):
            result[i] = dfs(0, i)
        return result