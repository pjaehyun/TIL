class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        hq = []

        for i in range(k):
            heapq.heappush(hq, (-nums[i], i))
        
        l, r = 0, k
        answer = []
        while r <= len(nums):
            n, idx = heapq.heappop(hq)
            if l <= idx <= r:
                answer.append(-n)
                heapq.heappush(hq, (n, idx))
            else:
                continue
            if r < len(nums):
                heapq.heappush(hq, (-nums[r], r))
            l += 1
            r += 1
        return answer
        