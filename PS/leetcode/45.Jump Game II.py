# 첫번째 풀이(bfs)
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        visited = set()

        if n == 1:
            return 0

        def bfs():
            dq = deque()
            dq.append((nums[0], 0, 0))

            while dq:
                value, idx, step = dq.popleft()

                for i in range(idx+1, idx+value+1):
                    if i == n-1:
                        return step + 1
                    if (nums[i], i) not in visited:
                        dq.append((nums[i], i, step + 1))
                        visited.add((nums[i], i))
        return bfs()

# 두번째 풀이(시간복잡도 개선)
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        step = 0
        prev, curr = 0, 0

        while curr < len(nums) - 1:
            prev, curr = curr + 1, max([idx + nums[idx] for idx in range(prev, curr+1)])
            step += 1
        return step