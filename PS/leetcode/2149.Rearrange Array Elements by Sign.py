class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)
        
        answer = []
        for i in range(len(positive)):
            answer.append(positive[i])
            answer.append(negative[i])

        return answer