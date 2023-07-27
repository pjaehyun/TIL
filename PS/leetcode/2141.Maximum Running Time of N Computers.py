class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(n, batteries, mid):
            return sum(min(x, mid) for x in batteries) >= mid*n


        l, r = 1, sum(batteries) // n
        while l < r:
            mid = (l + r + 1) // 2
            if check(n, batteries, mid):
                l = mid
            else:
                r = mid - 1
        return l