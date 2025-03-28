class Solution(object):
    def valid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def maxPoints(self, grid, queries):
        n, m = len(grid), len(grid[0])
        res = [0] * len(queries)
        q = sorted((queries[i], i) for i in range(len(queries)))
        visited = [[-1] * m for _ in range(n)]
        minh = [(grid[0][0], 0, 0)]
        visited[0][0] = 1
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        count = 0

        for val, idx in q:
            while minh and minh[0][0] < val:
                count += 1
                _, x, y = heapq.heappop(minh)
                for j in range(4):
                    newx, newy = x + dx[j], y + dy[j]
                    if self.valid(newx, newy, n, m) and visited[newx][newy] == -1:
                        visited[newx][newy] = 1
                        heapq.heappush(minh, (grid[newx][newy], newx, newy))
            res[idx] = count

        return res