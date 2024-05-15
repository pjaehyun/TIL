class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def bfs():
            dq = deque()

            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        score[i][j] = 0
                        dq.append((i, j))
            
            while dq:
                x, y = dq.popleft()
                step = score[x][y]
                
                for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                    if 0 <= nx < n and 0 <= ny < n and score[nx][ny] > step+1:
                        score[nx][ny] = step+1
                        dq.append((nx, ny))
        
        score = [[float('inf')] * n for _ in range(n)]
        bfs()
        
        visited = [[False] * n for _ in range(n)]
        hq = []
        heapq.heappush(hq, (-score[0][0], 0, 0))

        while hq:
            step, x, y = heapq.heappop(hq)
            step = -step

            if x == n-1 and y == n-1:
                return step
            
            visited[x][y] = True

            for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    s = min(step, score[nx][ny])
                    heapq.heappush(hq, (-s, nx, ny))
                    visited[nx][ny] = True
        return -1
