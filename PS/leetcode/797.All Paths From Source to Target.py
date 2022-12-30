# 백트래킹
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []

        def dfs(path, curr):
            if curr == len(graph) - 1:
                answer.append(path[:])
                return
            for g in graph[curr]:
                path.append(g)
                dfs(path[:], g)
                path.pop()
        dfs([0], 0)
        return answer

# dfs
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = []
        def dfs(path, curr):
            if curr == len(graph) - 1:
                answer.append(path[:])
                return
            for g in graph[curr]:
                dfs(path + [g], g)
        dfs([0], 0)
        return answer