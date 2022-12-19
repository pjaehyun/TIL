class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {x:[] for x in range(n)}
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        dq = deque()
        visited = set()
        dq.append(source)
        visited.add(source)
        
        while dq:
            cur = dq.popleft()
            if cur == destination:
                return True
            for g in graph[cur]:
                if g not in visited:
                    dq.append(g)
                    visited.add(g)
        return False