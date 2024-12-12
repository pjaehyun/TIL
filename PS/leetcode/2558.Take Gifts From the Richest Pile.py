class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        hq = []

        for i in range(len(gifts)):
            heapq.heappush(hq, -gifts[i])
        
        while k > 0:
            pile = heapq.heappop(hq)
            pile = -pile
            pile = int(pile**0.5)
            heapq.heappush(hq, -pile)
            k -= 1
        return -sum(hq)
        