class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        routes = set()
        graph = defaultdict(list)

        for i, j in connections:
            routes.add((i, j))
            graph[i].append(j)
            graph[j].append(i)

        answer = 0
        
        dq = deque()
        dq.append((0, -1))
        
        while dq:
            node, parent = dq.popleft()
            if (parent, node) in routes:
                answer += 1

            for child in graph[node]:
                if child == parent:
                    continue
                dq.append((child, node))
        return answer