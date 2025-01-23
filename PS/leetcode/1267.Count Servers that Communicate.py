class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(x, y):
            dq = deque()
            
            dq.append((x, y))
            res = 1
            while dq:
                x, y = dq.popleft()
                
                for i in range(m):
                    if i == x: continue
                    if grid[i][y] == 1:
                        grid[i][y] = 0
                        dq.append((i, y))
                        res += 1
                
                for j in range(n):
                    if j == y: continue
                    if grid[x][j] == 1:
                        grid[x][j] = 0
                        dq.append((x, j))
                        res += 1

            return res
        
        answer= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    res = bfs(i, j)
                    if res > 1:
                        answer += res
        return answer