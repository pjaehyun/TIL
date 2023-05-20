# 첫번째 풀이(BFS)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)

        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1.0 / values[i]
        
        answer = []
        for x, y in queries:
            if x not in graph or y not in graph:
                answer.append(-1.0)
            else:
                dq = deque()
                dq.append((x, 1.0))
                visited = set()
                visited.add(x)

                check = False

                while dq:
                    curr, dist = dq.popleft()
                    if curr == y:
                        answer.append(dist)
                        check = True
                        break
                    for neib in graph[curr]:
                        if neib not in visited:
                            visited.add(neib)
                            dq.append((neib, graph[curr][neib] * dist))
                if not check:
                    answer.append(-1.0)
        return answer
                
# 두번째 풀이(DFS)
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def dfs(start, end, dist):
            if start == end:
                temp[0] = dist
                return
            for neib, weight in graph[start].items():
                if neib not in visited:
                    visited.add(neib)
                    dfs(neib, end, dist * weight)

        graph = defaultdict(dict)

        for i in range(len(equations)):
            graph[equations[i][0]][equations[i][1]] = values[i]
            graph[equations[i][1]][equations[i][0]] = 1.0 / values[i]
        
        answer = []
        for x, y in queries:
            if x not in graph or y not in graph:
                answer.append(-1.0)
            else:
                visited = set()
                visited.add(x)
                temp = [-1.0]
                dfs(x, y, 1.0)
                answer.append(temp[0])

        return answer