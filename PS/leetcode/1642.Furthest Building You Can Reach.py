class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hq = []

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]

            if diff <= 0:
                continue
            
            bricks -= diff
            x = heapq.heappush(hq, -diff)

            if bricks < 0:
                bricks += -heapq.heappop(hq)
                ladders -= 1
            
            if ladders < 0:
                return i
        return len(heights) - 1