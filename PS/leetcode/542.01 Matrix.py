class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dq = deque()
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dq.append((i, j, 0))
                    visited[i][j] = True
        
        while dq:
            x, y, dist = dq.popleft()
            for xx, yy in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy]:
                    visited[xx][yy] = True
                    mat[xx][yy] = dist + 1
                    dq.append((xx, yy, dist + 1))
        return mat