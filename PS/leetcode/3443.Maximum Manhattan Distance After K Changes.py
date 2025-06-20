class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        res = 0
        for dirr in 'NE','SE','SW','NW':
            kk, dist = k, 0
            for c in s:
                dist += c in dirr or kk>0 or -1
                kk -= c not in dirr
                res = max(res, dist)
        
        return res