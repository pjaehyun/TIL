class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = 0
        answer = 0

        scores = zip(nums1, nums2)
        scores = sorted(scores, key=lambda x: -x[1])
        hq = []
        for score in scores:
            num1, num2 = score
            heapq.heappush(hq, num1)
            total += num1
            if len(hq) > k:
                total -= heapq.heappop(hq)
            if len(hq) == k:
                answer = max(answer, total * num2)
        return answer