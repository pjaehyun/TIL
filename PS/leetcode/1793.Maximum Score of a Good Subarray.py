class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = _min = nums[k]
        i = j = k
        n = len(nums)

        while i > 0 or j < n-1:
            if i == 0:
                j += 1
            elif j == n - 1:
                i -= 1
            elif nums[i-1] < nums[j+1]:
                j += 1
            else:
                i -= 1
            _min = min(_min, min(nums[i], nums[j]))
            res = max(res, _min * (j - i + 1))
        return res