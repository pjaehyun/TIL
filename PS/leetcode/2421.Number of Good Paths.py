# 해결하지 못해서 정답 참고해서 문제 풀이
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        answer = n = len(vals)
        uf = list(range(n))
        count = [Counter({vals[i]:1}) for i in range(n)]
        edges = sorted([max(vals[i], vals[j]), i, j] for i, j in edges)
        
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def union(v, x, y):
            nonlocal answer
            rootX, rootY = find(x), find(y)
            countX, countY = count[rootX][v], count[rootY][v]
            answer += countX * countY
            uf[rootY] = rootX
            count[rootX] = Counter({v:countX + countY})

        for v, x, y in edges:
            union(v, x, y)
            
        return answer