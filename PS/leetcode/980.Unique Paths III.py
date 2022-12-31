# 첫번째 풀이
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = []
        
        check = [[False] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        start = [0, 0]
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != -1:
                    check[i][j] = True
                if grid[i][j] == 1:
                    start[0], start[1] = i, j
                    visited[i][j] = True

        dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
        def dfs(x, y):
            if grid[x][y] == 2 and visited == check:
                answer.append(1)
                return
            for i in range(4):
                xx, yy = dx[i] + x, dy[i] + y
                if 0 <= xx < n and 0 <= yy < m and not visited[xx][yy] and grid[xx][yy] != -1:
                    visited[xx][yy] = True
                    dfs(xx, yy)
                    visited[xx][yy] = False
        
        dfs(start[0], start[1])
        return sum(answer)

# 두번째 풀이(리턴받는 방식 및 코드 개선)
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])        
        start = [0, 0]
        all_path = 2

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start[0], start[1] = i, j
                if grid[i][j] == 0:
                    all_path += 1

        def dfs(x, y, curr):
            if grid[x][y] == -1:
                return 0
            if grid[x][y] == 2:
                if curr == all_path:
                    return 1
                return 0
            
            grid[x][y] = -1
            result = 0
            for xx, yy in [[x,y+1],[x+1,y],[x-1,y],[x,y-1]]:
                if 0 <= xx < n and 0 <= yy < m:
                    result += dfs(xx, yy, curr + 1)
            grid[x][y] = 0
            return result
        return dfs(start[0], start[1], 1)
        