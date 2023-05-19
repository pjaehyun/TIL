class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        colors = [0] * n

        for i in range(n):
            if colors[i] != 0:
                continue
            
            dq = deque()
            dq.append(i)
            colors[i] = 1

            while dq:
                curr = dq.popleft()

                for neib in graph[curr]:
                    if colors[neib] == 0:
                        colors[neib] = -colors[curr]
                        dq.append(neib)
                    elif colors[neib] != -colors[curr]:
                        return False
        return True
