class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        res = 0
        for num in nums:
            digits = 0
            while num > 0:
                num //= 10
                digits += 1
            if not digits % 2:
                res += 1
        return res