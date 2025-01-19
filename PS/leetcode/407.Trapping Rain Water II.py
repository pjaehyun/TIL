import heapq

class Solution:
    def trapRainWater(self, height):
        n = len(height)
        m = len(height[0])

        pq = [] 
        vis = [[False] * m for _ in range(n)]

        for i in range(n):
            vis[i][0] = True
            vis[i][m - 1] = True
            heapq.heappush(pq, (height[i][0], i, 0))
            heapq.heappush(pq, (height[i][m - 1], i, m - 1))

        for i in range(m):
            vis[0][i] = True
            vis[n - 1][i] = True
            heapq.heappush(pq, (height[0][i], 0, i))
            heapq.heappush(pq, (height[n - 1][i], n - 1, i))

        ans = 0
        dr = [-1, 0, 1, 0]
        dc = [0, -1, 0, 1]

        while pq:
            h, r, c = heapq.heappop(pq)

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < n and 0 <= nc < m and not vis[nr][nc]:
                    ans += max(0, h - height[nr][nc])
                    heapq.heappush(pq, (max(h, height[nr][nc]), nr, nc))
                    vis[nr][nc] = True

        return ans