class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        visited = set()

        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        def dfs(node):
            visited.add(node)

            answer = sum([dfs(n) for n in graph[node] if n not in visited])
            if not answer and not hasApple[node]:
                return 0
            
            return answer + 2
        
        return max(0, dfs(0) - 2)