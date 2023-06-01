class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
        visited = [[False] * n for _ in range(n)]

        dq = deque()
        dq.append((0, 0, 1))
        grid[0][0] = 1
        while dq:
            x, y, d = dq.popleft()
            if x == n-1 and y == n-1:
                return d
            for i in range(8):
                xx, yy = x + dx[i], y + dy[i]
                if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 0:
                    grid[xx][yy] = 1
                    dq.append((xx, yy, d+1))
        return -1