class Solution:
    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        r,d = range(len(g)),defaultdict(SortedList)
        for i,j in product(r,r): d[i-j].add(g[i][j])
        return [[d[i-j].pop(-(i>=j)) for j in r] for i in r]