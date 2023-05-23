class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = nums
        heapq.heapify(self.hq)

        while self.k < len(self.hq):
            heapq.heappop(self.hq)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)

        while self.k < len(self.hq):
            heapq.heappop(self.hq)
        return self.hq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)