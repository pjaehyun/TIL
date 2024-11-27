class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def bfs(x):
            dq = deque()
            dq.append((x, 0))
            visited = [False] * n
            visited[x] = True
            while dq:
                curr, step = dq.popleft()
                if curr == n-1:
                    return step
                
                for neib in graph[curr]:
                    if not visited[neib]:
                        visited[neib] = True
                        dq.append((neib, step + 1))
            return -1
        graph = defaultdict(list)
        
        for i in range(n-1):
            graph[i].append(i+1)
        answer = []
        for a, b in queries:
            graph[a].append(b)

            answer.append(bfs(0))
        return answer