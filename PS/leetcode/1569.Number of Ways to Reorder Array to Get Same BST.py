class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(arr):
            if len(arr) <= 2: return 1
            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            return comb(len(left) + len(right), len(right)) * dfs(left) * dfs(right)
        return (dfs(nums) - 1) % (10**9 + 7)