class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        answer = [0] * n
        
        def dfs(curr, parent):
            nonlocal answer
            count = Counter()
            for n in graph[curr]:
                if n != parent:
                    count += dfs(n, curr)
            count[labels[curr]] += 1
            answer[curr] = count[labels[curr]]
            return count
        
        dfs(0, -1)
        return answer