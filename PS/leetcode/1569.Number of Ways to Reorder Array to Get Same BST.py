# 풀이 과정은 얼추 맞췄지만 해답을 내지 못하여 다른 풀이 참고하여 풀이
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(arr):
            if len(arr) <= 2: return 1
            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            return comb(len(left) + len(right), len(right) * dfs(left) * dfs(right))
        return dfs(nums) - 1