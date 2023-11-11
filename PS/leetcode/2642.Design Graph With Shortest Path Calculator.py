class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph =[[] for _ in range(n)]

        for edge in edges:
            self.graph[edge[0]].append((edge[1], edge[2]))


    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        
        hq = []
        heapq.heappush(hq, (0, node1))

        distances = [float('inf') for _ in range(self.n)]
        
        while hq:
            dist, curr = heapq.heappop(hq)
            if curr == node2:
                return dist
            for neib, weight in self.graph[curr]:
                if dist + weight < distances[neib]:
                    distances[neib] = dist + weight
                    heapq.heappush(hq, (dist + weight, neib))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)