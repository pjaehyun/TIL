class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(parent, curr, visited):
            visited[curr] = True
            for neib in graph[curr]:
                if not visited[neib]:
                    answer[neib].append(parent)
                    dfs(parent, neib, visited)

        graph = defaultdict(list)
        answer = [[] for _ in range(n)]
        
        for s, e in edges:
            graph[s].append(e)
        
        for i in range(n):
            dfs(i, i, [False] * n)
            answer[i].sort()
        return answer