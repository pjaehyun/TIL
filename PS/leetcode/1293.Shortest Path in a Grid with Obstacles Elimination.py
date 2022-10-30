class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n, b = len(grid), len(grid[0]), k

        if k >= m + n - 3:
            return m + n - 2
            
        dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
        visited = set()
        def bfs():
            dq = deque()
            dq.append((0,0,b,0))
            
            while dq:
                x, y, crush, distance = dq.popleft()
                if x == m - 1 and y == n - 1:
                    return distance
                
                for i in range(4):
                    xx, yy = x + dx[i], y + dy[i]
                    if 0 <= xx < m and 0 <= yy < n and crush >= grid[xx][yy]:
                        if (xx, yy, crush-grid[xx][yy]) not in visited:
                            dq.append((xx, yy, crush-grid[xx][yy], distance+1))
                            visited.add((xx, yy, crush-grid[xx][yy]))
            return -1
        return bfs()