class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]        
        n = len(grid)
        distance = 0
        dq = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dq.append((i, j))
        
        if len(dq) == n*n:
            return -1

        while dq:
            size = len(dq)
            distance += 1      

            for _ in range(size):
                x, y = dq.popleft()
                for i in range(4):
                    xx, yy = dx[i] + x, dy[i] + y
                    if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 0:
                        dq.append((xx, yy))
                        grid[xx][yy] = 1
        return distance - 1
                    
