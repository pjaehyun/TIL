class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
            
        def bfs(x, y):
            
            hq = []
            heapq.heappush(hq, (0, x, y))

            visited = [[False] * n for _ in range(m)]
            visited[x][y] = True

            while hq:
                t, x, y = heapq.heappop(hq)

                if (x, y) == (m-1, n-1):
                    return t
                
                for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                    if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                        next_time = t + 1
                        if grid[nx][ny] > next_time:
                            next_time += (grid[nx][ny] - t) // 2 * 2
                        visited[nx][ny] = True
                        heapq.heappush(hq, (next_time, nx, ny))
            return -1
        return bfs(0, 0)