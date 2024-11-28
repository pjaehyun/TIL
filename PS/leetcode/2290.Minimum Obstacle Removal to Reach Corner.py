class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]

        def bfs(x, y):
            dq = deque()
            dq.append((x, y, 0))
            visited[x][y] = True
            while dq:
                x, y, wall = dq.popleft()
                if x == n-1 and y == m-1:
                    return wall
                for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                        if grid[nx][ny] == 1:
                            dq.append((nx, ny, wall + 1))
                        else:
                            dq.appendleft((nx, ny, wall))
                        visited[nx][ny] = True
            return -1
        return bfs(0, 0)