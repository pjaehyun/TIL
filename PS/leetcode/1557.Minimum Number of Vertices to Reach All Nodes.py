class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree = [0] * n

        for x, y in edges:
            indegree[y] += 1
        
        answer = []
        for i in range(n):
            if indegree[i] == 0:
                answer.append(i)
        return answer