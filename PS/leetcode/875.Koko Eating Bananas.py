class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            k = sum(ceil(x / mid) for x in piles)
            if k > h:
                left = mid + 1
            else:
                right = mid
        return left