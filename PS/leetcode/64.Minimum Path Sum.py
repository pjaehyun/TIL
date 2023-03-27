class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    if j != 0:
                        grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0: 
                    if i != 0:
                        grid[i][j] = grid[i][j] + grid[i-1][j]
                else:
                    grid[i][j] = grid[i][j] + min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]