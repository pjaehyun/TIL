# BFS로 풀이 실패 후 다른 풀이 참고하여 DFS로 풀이
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visited = [False] * n
        ranks = [inf] * n

        def dfs(node, rank):
            if visited[node] or node == -1:
                return -1
            
            if ranks[node] < rank:
                return rank - ranks[node]
            
            ranks[node] = rank
            val = dfs(edges[node], rank+1)
            visited[node] = True

            return val
        answer = -1
        for i in range(n):
            answer = max(answer, dfs(i, 0))
        return answer
        