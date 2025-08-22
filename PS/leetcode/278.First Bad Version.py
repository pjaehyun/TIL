class Solution:
    def firstBadVersion(self, n):
        l, h = 0, n
        while l <= h:
            mid = l + (h - l) // 2
            if isBadVersion(mid):
                h = mid - 1
            else:
                l = mid + 1
        return l