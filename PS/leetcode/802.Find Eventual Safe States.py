# 첫번째 풀이(Dfs)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        answer = []
        def dfs(curr):
            answer = True
            for neib in graph[curr]:
                if visited[neib] or safe[neib] == 2:
                    answer = False
                    break
                if safe[neib] == 1:
                    continue
                visited[neib] = True
                if not dfs(neib):
                    answer = False
                visited[neib] = False
            safe[curr] = 1 if answer else 2
            return answer
        
        safe = [0] * n
        visited = [False] * n
        for i in range(n):
            if safe[i] == 0:
                visited[i] = True
                dfs(i)
                visited[i] = False
        
        for i in range(n):
            if safe[i] == 1:
                answer.append(i)
        return answer
    
# 두번째 풀이(Topological Sort)
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        c_graph = {x:[] for x in range(len(graph))}
        in_degree = {x:0 for x in range(len(graph))}
        for i in range(len(graph)):
            for j in graph[i]:
                c_graph[j].append(i)
                in_degree[i] += 1
        
        dq = deque()
        for k, v in in_degree.items():
            if v == 0:
                dq.append(k)
        answer = []
        while dq:
            curr = dq.popleft()
            answer.append(curr)
            
            for neib in c_graph[curr]:
                in_degree[neib] -= 1
                if in_degree[neib] == 0:
                    dq.append(neib)
        return sorted(answer)