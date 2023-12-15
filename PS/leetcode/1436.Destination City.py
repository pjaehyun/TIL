class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        n = len(paths)

        graph = defaultdict(str)
        indegree = defaultdict(int)

        for i in range(n):
            graph[paths[i][0]] = paths[i][1]
            indegree[paths[i][1]] += 1

        start = ""
        for k, v in graph.items():
            if indegree[k] == 0:
                start = k
                break
        
        answer = ""

        def dfs(city):
            nonlocal answer
            if graph[city] == "":
                answer = city
                return
            dfs(graph[city])
        dfs(start)
        return answer
        