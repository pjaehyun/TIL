# 첫번째 풀이(dfs)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x:[] for x in range(numCourses)}
        check = {x:0 for x in range(numCourses)}

        for p in prerequisites:
            graph[p[0]].append(p[1])
        
        def dfs(node):
            res = True
            for neib in graph[node]:
                if check[neib] == 2 or visited[neib]:
                    res = False
                    break
                if check[neib] == 1:
                    continue
                visited[neib] = True
                if not dfs(neib):
                    res = False
                visited[neib] = False
            check[node] = 1 if res else 2
            return res

        for i in range(numCourses):
            visited = [False] * numCourses
            if check[i] == 0:
                visited[i] = True
                if not dfs(i):
                    return False
                visited[0] = False
        return True
    
# 두번째 풀이(Topological Sort)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {x:[] for x in range(numCourses)}
        in_degree = {x:0 for x in range(numCourses)}

        for p in prerequisites:
            graph[p[1]].append(p[0])
            in_degree[p[0]] += 1
        dq = deque()
        
        for k, v in in_degree.items():
            if v == 0:
                dq.append(k)

        answer = []
        while dq:
            curr = dq.popleft()
            answer.append(curr)

            for neib in graph[curr]:
                in_degree[neib] -= 1
                if in_degree[neib] == 0:
                    dq.append(neib)
        return len(answer) == numCourses