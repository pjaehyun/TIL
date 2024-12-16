class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)

        answer = [0] * n

        nums = [(num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(nums)
        for _ in range(k):
            num, idx = heapq.heappop(nums)

            heapq.heappush(nums, (num*multiplier, idx))
        
        for i in range(n):
            answer[nums[i][1]] = nums[i][0]
        return answer