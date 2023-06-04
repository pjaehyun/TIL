class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                if isConnected[i-1][j-1] == 1:
                    graph[i].append(j)
        
        def dfs(node):
            for neib in graph[node]:
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib)
        
        visited = set()
        answer = 0
        for i in range(1, n+1):
            if i not in visited:
                visited.add(i)
                answer += 1
                dfs(i)
        return answer