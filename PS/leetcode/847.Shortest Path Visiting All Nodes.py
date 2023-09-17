class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        num_nodes = len(graph)
        all_visited_mask = (1 << num_nodes) - 1
        q = deque()

        visited = [[False for _ in range(num_nodes)] for _ in range(all_visited_mask + 1)]

        for node in range(num_nodes):
            initial_mask = (1 << node)
            q.append((node, initial_mask, 1))
            visited[initial_mask][node] = True

        while q:
            current = q.popleft()
            current_node, current_mask, current_length = current

            if current_mask == all_visited_mask:
                return current_length - 1

            for neighbor in graph[current_node]:
                new_mask = current_mask | (1 << neighbor)

                if visited[new_mask][neighbor]:
                    continue

                q.append((neighbor, new_mask, current_length + 1))
                visited[new_mask][neighbor] = True

        return -1