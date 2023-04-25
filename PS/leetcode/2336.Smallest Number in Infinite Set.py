class SmallestInfiniteSet:

    def __init__(self):
        self.hq = []
        for i in range(1, 1001):
            heapq.heappush(self.hq, i)
        

    def popSmallest(self) -> int:
        return heapq.heappop(self.hq)
        

    def addBack(self, num: int) -> None:
        if num not in self.hq:
            heapq.heappush(self.hq, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)