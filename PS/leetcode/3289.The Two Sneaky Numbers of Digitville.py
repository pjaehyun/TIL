class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        answer = []
        for num in nums:
            count[num] += 1

            if count[num] > 1:
                answer.append(num)
        return answer