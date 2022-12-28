class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-x for x in piles]
        heapq.heapify(max_heap)
        
        for i in range(k):
            n = -heapq.heappop(max_heap)
            n = n - floor(n / 2)
            heapq.heappush(max_heap, -n)
        return -sum(max_heap)