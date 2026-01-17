class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        best = 0
        n = len(bottomLeft)
        for i in range(n):
            for j in range(i):
                w = self._calc_intersection(bottomLeft[i][0], topRight[i][0], bottomLeft[j][0], topRight[j][0])
                h = self._calc_intersection(bottomLeft[i][1], topRight[i][1], bottomLeft[j][1], topRight[j][1])
                side = w if w < h else h
                if side > best:
                    best = side
        return best * best

    def _calc_intersection(self, a1, b1, a2, b2):
        x1, y1, x2, y2 = a1, b1, a2, b2
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        if y1 <= x2:
            return 0
        if y1 <= y2:
            return y1 - x2
        return y2 - x2