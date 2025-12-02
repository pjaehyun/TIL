class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        y_coor = defaultdict(int)

        for x, y in points:
            y_coor[y] += 1
        
        r, s = 0, 0
        for v in y_coor.values():
            if v >= 2:
                c = v*(v-1)//2

                r += c*s
                s += c
        return r % (10**9+7)