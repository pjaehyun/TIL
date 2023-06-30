# 이진탐색을 사용하지 않고 풀었을 때 시간초과 
# 정확한 해답을 못찾아 다른 풀이방식 참고하여 해결
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def bfs(row, col, cells, mid):
            graph = [[0]*col for _ in range(row)]
            dq = deque()

            for x, y in cells[:mid]:
                graph[x-1][y-1] = 1

            for i in range(col):
                if graph[0][i] == 0:
                    dq.append((0, i))
                    graph[0][i] = -1

            while dq:
                x, y = dq.popleft()
                if x == row - 1:
                    return True
                
                for xx, yy in [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]:
                    if 0 <= xx < row and 0 <= yy < col and graph[xx][yy] == 0:
                        dq.append((xx, yy))
                        graph[xx][yy] = -1
            return False
        
                        
        left, right = 1, row * col
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            
            if bfs(row, col, cells, mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer