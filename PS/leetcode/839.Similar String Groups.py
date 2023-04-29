# 첫번째 풀이(BFS, DFS(stack), DFS(recursion)
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def dfs_stack(start):
            stack = [start]

            while stack:
                curr = stack.pop()

                for neib in graph[curr]:
                    if not visited[neib]:
                        visited[neib] = True
                        stack.append(neib)

        def dfs_recursion(start):
            for neib in graph[start]:
                if not visited[neib]:
                    visited[neib] = True
                    dfs_recursion(neib)

        def bfs(start):
            dq = deque([start])
            
            while dq:
                curr = dq.popleft()

                for neib in graph[curr]:
                    if not visited[neib]:
                        visited[neib] = True
                        dq.append(neib)

        n = len(strs)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                
                if count == 0 or count == 2:
                    graph[i].append(j)
                    graph[j].append(i)
        
        visited = [False] * n
        answer = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                # dfs_stack(i)
                # dfs_recursion(i)
                answer += 1
        return answer

# 두번째 풀이(Union-Find)
class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                self.parent[py] = px
            elif self.rank[px] < self.rank[py]:
                self.parent[px] = py
            else:
                self.parent[py] = px
                self.rank[px] += 1
            
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        n = len(strs)
        
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        count += 1
                
                if count == 0 or count == 2:
                    edges.append([i, j])
        
        uf = UnionFind(n)
        for x, y in edges:
            uf.union(x, y)
        
        answer = set()
        for i in range(n):
            answer.add(uf.find(i))
        return len(answer)