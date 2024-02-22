# 첫번째 풀이
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
    
# 두번째 풍리 
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        in_degree = [0] * (N + 1)
        out_degree = [0] * (N + 1)
        for a in trust:
            out_degree[a[0]] += 1
            in_degree[a[1]] += 1
        for i in range(1, N + 1):
            if in_degree[i] == N - 1 and out_degree[i] == 0:
                return i
        return -1