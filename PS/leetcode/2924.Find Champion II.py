class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = {x:x for x in range(n)}

        for edge in edges:
            graph[edge[1]] = edge[0]
        
        answer = None
        check = 0
        for i in range(n):
            if graph[i] == i:
                answer = i
                check += 1
        return answer if check == 1 else -1