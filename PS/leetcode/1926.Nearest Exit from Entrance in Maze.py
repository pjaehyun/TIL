class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
        visited = [[False] * n for _ in range(m)]
        def bfs():
            dq = deque()
            dq.append((entrance[0], entrance[1], 0))
            visited[entrance[0]][entrance[1]] = True
            while dq:
                x, y, d = dq.popleft()
                for i in range(4):
                    xx, yy = dx[i] + x, dy[i] + y
                    if 0 <= xx < m and 0 <= yy < n and not visited[xx][yy] and maze[xx][yy] == '.':
                        if xx == 0 or xx == m-1 or yy == 0 or yy == n-1:
                            return d + 1
                        dq.append((xx, yy, d+1))
                        visited[xx][yy] = True
        answer = bfs()
        if answer:
            return answer
        return -1