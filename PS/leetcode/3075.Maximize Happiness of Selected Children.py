# 첫번째 풀이
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness = [-x for x in happiness]
        heapq.heapify(happiness)
        
        turn = 0
        answer = 0
        for _ in range(k):
            v = heapq.heappop(happiness)
            v = -v
            answer += (v - turn) if v > turn else 0
            turn += 1
        return answer

# 두번째 풀이
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum([x - idx if x > idx else 0 for idx, x in enumerate(sorted(happiness, reverse=True))][:k])