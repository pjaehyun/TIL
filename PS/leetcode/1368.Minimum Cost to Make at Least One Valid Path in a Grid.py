class Solution(object):
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        minCost = [[float('inf')] * n for _ in range(m)]
        minCost[0][0] = 0
        
        dque = deque([(0, 0)])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while dque:
            r, c = dque.popleft()
            
            for i, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc
                cost = 1 if grid[r][c] != i + 1 else 0
                
                if 0 <= nr < m and 0 <= nc < n and minCost[r][c] + cost < minCost[nr][nc]:
                    minCost[nr][nc] = minCost[r][c] + cost
                    
                    if cost == 1:
                        dque.append((nr, nc))
                    else:
                        dque.appendleft((nr, nc))
        
        return minCost[m - 1][n - 1]