class Solution:
    def findScore(self, nums: List[int]) -> int:
        dq = deque(sorted([(x, idx) for idx, x in enumerate(nums)], key=lambda x: (x[0], x[1])))
        
        answer = 0
        visited = [False] * len(nums)
        while dq:
            num, idx = dq.popleft()
            
            if not visited[idx]:
                visited[idx] = True
                if idx + 1 < len(nums):
                    visited[idx+1] = True

                if idx - 1 >= 0:
                    visited[idx-1] = True

                answer += num
        return answer