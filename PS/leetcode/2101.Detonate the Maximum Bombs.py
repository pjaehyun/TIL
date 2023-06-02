class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        n, answer = len(bombs), 0
        graph = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i].append(j)
        
        def dfs(node):
            nonlocal count
            for neib in graph[node]:
                if not visited[neib]:
                    count += 1
                    visited[neib] = True
                    dfs(neib)

        for i in range(n):
            count = 1
            visited = [False] * n
            visited[i] = True
            dfs(i)
            answer = max(answer, count)
        return answer