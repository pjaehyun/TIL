class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])        
        answer = [[-1] * n for _ in range(m)]
        dq = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    answer[i][j] = 0
                    dq.append((i, j))
        
        while dq:
            x, y = dq.popleft()
            for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0<=nx<m and 0<=ny<n and answer[nx][ny] == -1:
                    answer[nx][ny] = answer[x][y] + 1
                    dq.append((nx, ny))
        return answer