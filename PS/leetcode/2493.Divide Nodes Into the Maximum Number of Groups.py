class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:

        def is_bipartite(node, c):
            color[node] = c
            components.append(node)
            for neighbor in graph[node]:
                if (not color[neighbor] and not is_bipartite(neighbor, -1*c)
                    or color[neighbor] == c):
                    return False
            return True

        def find_depth(root):
            visited = [0] * n
            que, visited[root], depth = deque([root]), 1, 0
            while que:
                for _ in range(len(que)):
                    for neighbor in graph[que.popleft()]:
                        if not visited[neighbor]:
                            que.append(neighbor)
                            visited[neighbor] = 1
                depth += 1
            return depth


        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[v-1].append(u-1)
            graph[u-1].append(v-1)

        ans, color = 0, [0] * n
        for node in range(n):
            if not color[node]:
                components = []
                if not is_bipartite(node, 1):
                    return -1
                ans += max(find_depth(node) for node in components)
        return ans