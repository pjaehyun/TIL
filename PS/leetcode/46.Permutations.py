class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_length = len(nums)
        result = []
        visited = [False] * nums_length
        
        def dfs(arr):
            if len(arr) == nums_length:
                result.append(arr[:])

            for i in range(nums_length):
                if not visited[i]:
                    visited[i] = True
                    arr.append(nums[i])
                    dfs(arr)
                    arr.pop()
                    visited[i] = False
        dfs([])
        return result