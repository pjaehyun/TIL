class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}

        def find(x):
            if x not in UF:
                UF[x] = x
            
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
                

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX > rootY:
                UF[rootX] = rootY
            else:
                UF[rootY] = rootX
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        answer = ""
        for s in baseStr:
            answer += find(s)
        return answer
            