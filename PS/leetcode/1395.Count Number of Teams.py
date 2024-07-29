from sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        sl1 = SortedList()
        sl2 = SortedList(rating)
        res = 0
        for j in range(len(rating)):
            sl2.remove(rating[j])
            sl1Index = bisect.bisect(sl1, rating[j])
            sl2Index = bisect.bisect(sl2, rating[j])
            res += sl1Index * (len(sl2) - sl2Index)
            res += (len(sl1) - sl1Index) * sl2Index
            sl1.add(rating[j])
        return res