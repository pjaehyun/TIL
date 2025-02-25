class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod = 10**9+7

        prefix = 0
        odd = 0
        even = 1

        for num in arr:
            prefix += num

            if prefix % 2 != 0:
                odd += 1
            else: even += 1
        return odd*even%mod