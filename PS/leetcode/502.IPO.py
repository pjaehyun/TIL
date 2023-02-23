class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        projects = sorted([(profits[i], capital[i]) for i in range(len(profits))], key=lambda x:x[1])

        hq = []
        i = 0
        for _ in range(k):
            while i < len(profits) and projects[i][1] <= w:
                heapq.heappush(hq, -projects[i][0])
                i += 1
            if not hq:
                break

            w += -heapq.heappop(hq)
        return w