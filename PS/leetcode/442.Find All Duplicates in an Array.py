class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        answer = []
        for k, v in count.items():
            if v > 1:
                answer.append(k)
        return answer