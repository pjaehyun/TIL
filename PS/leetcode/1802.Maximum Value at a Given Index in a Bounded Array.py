class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n

        left, right = 0, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            left_offset = max(mid - index, 0)
            res = (mid + left_offset) * (mid - left_offset + 1) // 2
            right_offset = max(mid - ((n - 1) - index), 0)
            res += (mid + right_offset) * (mid - right_offset + 1) // 2

            if res-mid <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left + 1