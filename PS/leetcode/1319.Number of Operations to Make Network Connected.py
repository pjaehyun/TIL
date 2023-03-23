# 첫번째 풀이(DFS)
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        def dfs(n):
            for node in graph[n]:
                if not visited[node]:
                    visited[node] = True
                    dfs(node)
        
        if len(connections) < n-1:
            return -1

        graph = defaultdict(list)

        for com1, com2 in connections:
            graph[com1].append(com2)
            graph[com2].append(com1)
        
        visited = [False] * n
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        return count - 1

# 두번째 풀이(BFS)
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        def bfs(n):
            dq = deque()
            dq.append(n)

            while dq:
                curr = dq.popleft()

                for node in graph[curr]:
                    if not visited[node]:
                        visited[node] = True
                        dq.append(node)
        
        if len(connections) < n-1:
            return -1

        graph = defaultdict(list)

        for c1, c2 in connections:
            graph[c1].append(c2)
            graph[c2].append(c1)
        
        visited = [False] * n

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                bfs(i)
        return count - 1

# 세번째 풀이(Union-Find)
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        def union(x, y):
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
        not_connect = n - 1
        cables = 0
        for com1, com2 in connections:
            com1_root = find(com1)
            com2_root = find(com2)
            if com1_root == com2_root:
                cables += 1
            else:
                not_connect -= 1
                union(com1, com2)

        return not_connect if cables >= not_connect else -1