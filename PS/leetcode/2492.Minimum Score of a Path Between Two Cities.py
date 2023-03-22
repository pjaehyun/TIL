# 첫번째 풀이(BFS)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for s, e, d in roads:
            graph[s].append((e, d))
            graph[e].append((s, d))

        dq = deque()
        dq.append(n)

        answer = inf
        while dq:
            node = dq.popleft()

            for nei, distance in graph[node]:
                answer = min(answer, distance)
                dq.append(nei)
            graph[node] = []

        return answer
        
# 두번째 풀이(DFS)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for s, e, d in roads:
            graph[s].append((e, d))
            graph[e].append((s, d))

        dq = deque()
        dq.append(n)

        answer = inf
        
        def dfs(node, distance):
            nonlocal answer
            answer = min(answer, distance)
            while graph[node]:
                nei, distance = graph[node].pop()
                dfs(nei, distance)
        
        dfs(n, inf)
        return answer

# 세번째 풀이(Union-Find)
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        UF = {x:[x, inf] for x in range(1, n+1)}
        
        def union(x, y, d):
            rootX = find(x)[0]
            rootY = find(y)[0]

            if rootX != rootY:
                if UF[rootX][1] <= UF[rootY][1]:
                    UF[rootY][0] = rootX
                    UF[rootX][1] = min(UF[rootX][1], d)
                elif UF[rootX][1] > UF[rootY][1]:
                    UF[rootX][0] = rootY
                    UF[rootY][1] = min(UF[rootY][1], d)
            else:
                UF[rootX][1] = min(UF[rootX][1], d)
                    
        
        def find(x):
            if x != UF[x][0]:
                UF[x][0] = find(UF[x][0])[0]
            return UF[x][0], UF[x][1]
        
        for x, y, d in roads:
            union(x, y, d)

        return UF[find(1)[0]][1]
        