class Solution:
    def find(self, node, parent):
        if parent[node] < 0:
            return node
        parent[node] = self.find(parent[node], parent)
        return parent[node]

    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        parent = [-1] * n
        minCost = [-1] * n

        for u, v, cost in edges:
            uRoot, vRoot = self.find(u, parent), self.find(v, parent)
            if uRoot != vRoot:
                minCost[uRoot] &= minCost[vRoot]
                parent[vRoot] = uRoot
            minCost[uRoot] &= cost

        result = []
        for u, v in query:
            uRoot, vRoot = self.find(u, parent), self.find(v, parent)
            if u == v:
                result.append(0)
            elif uRoot != vRoot:
                result.append(-1)
            else:
                result.append(minCost[uRoot])

        return result