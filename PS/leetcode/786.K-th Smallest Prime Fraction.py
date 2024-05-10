class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        hq = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(hq, (arr[i] / arr[j], arr[i], arr[j]))
        
        answer = None
        for _ in range(k):
            value, child, parent = heapq.heappop(hq)
            answer = [child, parent]
        return answer