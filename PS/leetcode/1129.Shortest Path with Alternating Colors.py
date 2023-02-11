class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for a, b in redEdges:
            graph[a].append(('r', b))
        for u, v in blueEdges:
            graph[u].append(('b', v))
        
        distances = [-1 for _ in range(n)]
        visited = set()
        dq = deque()
        
        for edge in graph[0]:
            dq.append((edge[0], edge[1], 1))
            visited.add((edge[0], 0, edge[1]))
        distances[0] = 0
        
        while dq:
            color, node, count = dq.popleft()
            if distances[node] != -1:
                distances[node] = min(distances[node], count)
            else:
                distances[node] = count

            if color == 'r':
                for edge in graph[node]:
                    if edge[0] == 'b' and (edge[0], node, edge[1]) not in visited:
                        dq.append((edge[0], edge[1], count + 1))
                        visited.add((edge[0], node, edge[1]))
            elif color == 'b':
                for edge in graph[node]:
                    if edge[0] == 'r' and (edge[0], node, edge[1]) not in visited:
                        dq.append((edge[0], edge[1], count + 1))
                        visited.add((edge[0], node, edge[1]))
        return distances
