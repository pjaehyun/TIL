class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.answer = 0
        def union(x, y):
            self.answer += 1
            rootX = find(x)
            rootY = find(y)

            if rootX > rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
        
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        
        UF = {x:x for x in range(n)}
        count = [0 for _ in range(n)]
        
        for u, v in edges:
            union(u, v)
        
        counter = Counter(find(x) for x in UF.values())
        counter = list(counter.values())
        
        first = counter[0]

        answer = 0
        for i in range(1, len(counter)):
            answer += first * counter[i]
            first += counter[i]

        return answer