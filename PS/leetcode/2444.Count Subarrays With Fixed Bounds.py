# 완전탐색으로 했을 때 시간초과로 실패
# 이 후 슬라이딩 윈도우로 시도하다가 못풀어서 다른 풀이 참고
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        answer = 0
        j = -1
        prev_min = -1
        prev_max = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                j = i
            if num == minK:
                prev_min = i
            if num == maxK:
                prev_max = i
            
            print(prev_min, prev_max, j)
            answer += max(0, min(prev_min, prev_max) - j)
        return answer