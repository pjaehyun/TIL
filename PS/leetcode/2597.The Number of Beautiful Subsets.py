class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        def backtracking(idx):
            nonlocal answer

            if n == idx:
                answer += 1
                return

            if nums[idx] - k not in visited and nums[idx] + k not in visited:
                visited[nums[idx]] += 1
                backtracking(idx+1)
                visited[nums[idx]] -= 1
                if visited[nums[idx]] == 0:
                    del visited[nums[idx]]
            
            backtracking(idx + 1)
        
        visited = defaultdict(int)
        backtracking(0)
        return answer - 1