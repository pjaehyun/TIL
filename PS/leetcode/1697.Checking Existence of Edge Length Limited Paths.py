class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        def union(x, y):
            rootX, rootY = find(x), find(y)

            if rootX < rootY:
                UF[rootY] = rootX
            else:
                UF[rootX] = rootY
        
        def find(x):
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]

        edgeList = sorted(edgeList, key=lambda x:x[2])
        UF = {x:x for x in range(n)}
        answer = [False] * len(queries)
        i = 0
        queries = sorted(enumerate(queries), key=lambda x:x[1][2])
        for idx, (s, e, limit) in queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            answer[idx] = (find(s) == find(e))
        return answer