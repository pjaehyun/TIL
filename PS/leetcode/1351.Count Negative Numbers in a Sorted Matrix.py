class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        row, col = m-1, 0

        answer = 0    
        while row >= 0 and col < n:
            if grid[row][col] < 0:
                answer += (n - col)
                row -= 1
            else:
                col += 1
        return answer
