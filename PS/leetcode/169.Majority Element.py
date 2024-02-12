class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = -1
        majority = 0
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] > majority:
                majority = count[num]
                answer = num
        return answer
            