class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        count = defaultdict(int)
        answer = -1
        for num in nums:
            if count[-num] > 0:
                answer = max(answer, abs(num))
            count[num] += 1
        return answer