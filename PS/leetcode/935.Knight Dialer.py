class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def dfs(n, x, y):
            if n == 0:
                return 1
            
            answer = 0
            for dx, dy in [[2,1],[1,2],[-2,1],[-1,2],[2,-1],[1,-2],[-2,-1],[-1,-2]]:
                nx, ny = x + dx, y + dy

                if (-1 < nx < 3 and -1 < ny < 3) or (nx == 3 and ny == 1):
                    answer += dfs(n-1, nx, ny)
            return answer % (10**9+7)
        answer = dfs(n-1, 3, 1)
        for x in range(3):
            for y in range(3):
                answer += dfs(n-1, x, y)
        return answer % (10**9+7)
