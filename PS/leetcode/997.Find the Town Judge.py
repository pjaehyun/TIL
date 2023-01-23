class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # graph[x] = [(trust), (trusted)]
        graph = {x:[0,0] for x in range(1, n+1)}

        for x, y in trust:
            graph[x][0] += 1
            graph[y][1] += 1
        
        for i in range(1, n+1):
            if graph[i][0] == 0 and graph[i][1] == n-1:
                return i
        return -1