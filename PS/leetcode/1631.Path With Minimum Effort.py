class Solution:
    def minimumEffortPath(self, hts: list[list[int]]) -> int:

        m,n, dx,dy = len(hts),len(hts[0]), 1,0
        ans, heap, unseen = 0, [(0, 0, 0)], set(product(range(m), range(n)))

        while heap:
            effort, x, y = heappop(heap)
            unseen.discard((x, y))
            ans = max(ans,effort)
            if (x,y) == (m-1, n-1): break

            for _ in range(4):
                X, Y, dx, dy = x + dx, y + dy, -dy, dx
                if (X,Y) in unseen:
                    heappush(heap, (abs(hts[x][y] - hts[X][Y]), X, Y))

        return ans