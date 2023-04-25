# 첫번째 풀이
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

# 두번째 풀이(딕셔너리를 이용한 시간복잡도 개선)
class SmallestInfiniteSet:

    def __init__(self):
        self.hq = []
        self.isExist = {}
        self.num = 1

    def popSmallest(self) -> int:
        if self.hq:
            min = heapq.heappop(self.hq)
            self.isExist[min] = 0
            return min
        self.num += 1
        return self.num - 1
        

    def addBack(self, num: int) -> None:
        if self.num > num and self.isExist.get(num, 0) == 0:
            heapq.heappush(self.hq, num)
            self.isExist[num] = 1
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)