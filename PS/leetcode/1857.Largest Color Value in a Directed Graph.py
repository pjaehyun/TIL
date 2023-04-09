# 다른 풀이 참고하여 풀이
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        n,k = len(colors), 26
        graph = [[] for _ in range(n)]
        indegree = [0 for x in range(n)]

        for s, e in edges:
          graph[s].append(e)
          indegree[e] += 1

        dq = deque()
        for i in range(len(indegree)):
          if indegree[i] == 0:
            dq.append(i)
        
        counts = [[0] * k for _ in range(n)]

        for idx, color in enumerate(colors):
            counts[idx][ord(color) - ord('a')] += 1
        
        max_count, visited = 0, 0

        while dq:
          curr = dq.popleft()
          visited += 1
          for neib in graph[curr]:
            for i in range(k):
              counts[neib][i] = max(counts[neib][i], counts[curr][i] + (ord(colors[neib]) - ord('a') == i))
            indegree[neib] -= 1
            if indegree[neib] == 0:
              dq.append(neib)
          max_count = max(max_count, max(counts[curr]))
        return max_count if visited == n else -1
