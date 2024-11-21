class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        def move(x, y):

            # up
            for i in range(x - 1, -1, -1):
                if graph[i][y] == 1 or graph[i][y] == 2:
                    break
                graph[i][y] = -1

            # down
            for i in range(x + 1, m):
                if graph[i][y] == 1 or graph[i][y] == 2:
                    break
                graph[i][y] = -1

            # left
            for i in range(y-1, -1, -1):
                if graph[x][i] == 1 or graph[x][i] == 2:
                    break
                graph[x][i] = -1

            # right
            for i in range(y+1, n):
                if graph[x][i] == 1 or graph[x][i] == 2:
                    break
                graph[x][i] = -1
        
        graph = [[0] * n for _ in range(m)]

        for wall in walls:
            graph[wall[0]][wall[1]] = 1

        for guard in guards:
            graph[guard[0]][guard[1]] = 2

        for guard in guards:
            move(guard[0], guard[1])
            
        answer = 0
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 0:
                    answer += 1
        return answer