class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        
        answer = -1
        for s, e in edges:
            graph[s] += 1
            graph[e] += 1

            if graph[s] > graph[e]:
                answer = s
            else:
                answer = e

        return answer