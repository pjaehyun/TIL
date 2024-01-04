class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        answer = 0
        for k, v in count.items():
            if v == 1:
                return -1
            answer += (v + 2) // 3
        return answer