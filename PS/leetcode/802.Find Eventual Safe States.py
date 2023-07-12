class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        answer = []
        def dfs(curr):
            answer = True
            for neib in graph[curr]:
                if visited[neib] or safe[neib] == 2:
                    answer = False
                    break
                if safe[neib] == 1:
                    continue
                visited[neib] = True
                if not dfs(neib):
                    answer = False
                visited[neib] = False
            safe[curr] = 1 if answer else 2
            return answer
        
        safe = [0] * n
        visited = [False] * n
        for i in range(n):
            if safe[i] == 0:
                visited[i] = True
                dfs(i)
                visited[i] = False
        
        for i in range(n):
            if safe[i] == 1:
                answer.append(i)
        return answer