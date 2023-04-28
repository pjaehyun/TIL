class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def bfs(start):
            dq = deque([start])
            
            while dq:
                curr = dq.popleft()

                for neib in graph[curr]:
                    if not visited[neib]:
                        visited[neib] = True
                        dq.append(neib)

        n = len(strs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                
                if count == 0 or count == 2:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False] * n
        answer = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                answer += 1
        return answer