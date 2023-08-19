# 크루스칼 알고리즘을 이용하여 탐색할 떄 여러가지 최소신장 트리를 구하는 부분에서 막혀
# 다른 풀이 참고하여 풀었다.
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:        
        def find(UF, x):
            if UF[x] != x:
                UF[x] = find(UF, UF[x])
            return UF[x]

        def union(UF, x, y):
            rX = find(UF, x)
            rY = find(UF, y)

            if rX > rY:
                UF[rX] = rY
            else:
                UF[rY] = rX
    
        def find_mst(n, edges, block, e):
            UF = {x:x for x in range(n)}
            weight = 0

            if e != -1:
                weight += edges[e][2]
                union(UF, edges[e][0], edges[e][1])
            
            for i in range(len(edges)):
                if i == block:
                    continue
                if find(UF, edges[i][0]) != find(UF, edges[i][1]):
                    union(UF, edges[i][0], edges[i][1])
                    weight += edges[i][2]
            
            for i in range(n):
                if find(UF, i) != find(UF, 0):
                    return float('inf')
            return weight

        critical, pseudo_critical = [], []
        
        for i in range(len(edges)):
            edges[i].append(i)
        edges.sort(key=lambda x:x[2])

        mst_weight = find_mst(n, edges, -1, -1)
        for i in range(len(edges)):
            if mst_weight < find_mst(n, edges, i, -1):
                critical.append(edges[i][3])
            elif mst_weight == find_mst(n, edges, -1, i):
                pseudo_critical.append(edges[i][3])
        return [critical, pseudo_critical]