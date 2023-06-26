# 첫번째 풀이
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap = []
        if 2 * candidates >= len(costs):
            for i in range(len(costs)):
                heapq.heappush(min_heap, costs[i])
            answer = 0
            for _ in range(k):
                answer += heapq.heappop(min_heap)
            return answer

        answer = 0
        left, right = 0, len(costs) - 1
        for i in range(candidates):
            heapq.heappush(min_heap, (costs[i], "left"))
            left += 1
        for i in range(len(costs)-1, len(costs) - candidates - 1, -1):
            heapq.heappush(min_heap, (costs[i], "right"))
            right -= 1
        
        for _ in range(k):
            num, direction = heapq.heappop(min_heap)
            answer += num
            if direction == "left":
                if left <= right: 
                    heapq.heappush(min_heap, (costs[left], "left"))
                    left += 1
            else:
                if left <= right: 
                    heapq.heappush(min_heap, (costs[right],"right"))
                    right -= 1
        return answer

# 두번째 풀이(코드 및 시간복잡도 개선)
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        left = costs[:candidates]
        right = costs[max(candidates, len(costs) - candidates):]
        heapq.heapify(left) 
        heapq.heapify(right)
        ln, rn = candidates, len(costs) - 1 - candidates

        answer = 0
        for _ in range(k):
            if not right or (left and left[0] <= right[0]):
                answer += heapq.heappop(left)
                if ln <= rn:
                    heapq.heappush(left, costs[ln])
                    ln += 1
            else:
                answer += heapq.heappop(right)
                if ln <= rn:
                    heapq.heappush(right, costs[rn])
                    rn -= 1
        return answer