class SummaryRanges:

    def __init__(self):
        self.arr = set()
        
    def addNum(self, value: int) -> None:
        self.arr.add(value)
        
    def getIntervals(self) -> List[List[int]]:
        result = []
        temp = sorted(self.arr)
        res = [-1, -1]
        while temp:
            n = temp.pop(0)
            if res[0] == -1:
                res[0], res[1] = n, n
            else:
                if res[-1] + 1 == n:
                    res[-1] = n
                else:
                    result.append(res[:])
                    res = [n, n]
        result.append(res[:])
        return result


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()