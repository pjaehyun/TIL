# 첫번째 풀이
class Solution:
    def maxSatisfaction(self, satisfaction: List[int], answer = 0) -> int:
        satisfaction.sort()
        
        for i in range(len(satisfaction)):
            answer = max(answer, sum([(idx+1) * v for idx, v in enumerate(satisfaction[i:])]))
        return answer

# 두번째 풀이(dp, 시간복잡도 개선)
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        total = 0
        curr = 0
        for v in satisfaction:
            curr += v
            if curr < 0:
                break
            total += curr
        return total
