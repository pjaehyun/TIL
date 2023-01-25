class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        graph = {i:edges[i] for i in range(len(edges))}
        answer = []

        dist1 = {}
        dist2 = {}

        def dfs(node, dist, step, visited):
            if graph[node] == -1:
                return
            if graph[node] not in visited:
                dist[graph[node]] = step + 1
                visited.add(graph[node])
                dfs(graph[node], dist, step+1, visited)

        dist1[node1] = 0
        visited1 = set()
        visited1.add(node1)
        dfs(node1, dist1, 0, visited1)

        dist2[node2] = 0
        visited2 = set()
        visited2.add(node2)
        dfs(node2, dist2, 0, visited2)
        
        for n, d in dist1.items():
            if n in dist2:
                answer.append([n, max(d, dist2[n])])
        
        answer.sort(key=lambda x:(x[1],x[0]))
        return answer[0][0] if answer else -1