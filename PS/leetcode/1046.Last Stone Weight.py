class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        
        for stone in stones:
            heapq.heappush(hq, -stone)
        
        while len(hq) > 1:
            y, x = -heapq.heappop(hq), -heapq.heappop(hq)
            heapq.heappush(hq, -(y - x))
        return -hq[0]
        