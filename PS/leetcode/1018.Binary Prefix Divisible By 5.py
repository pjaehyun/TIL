class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        sub = 0
        answer = []
        for num in nums:
            sub = (sub << 1) + num
            if sub % 5 == 0:
                answer.append(True)
            else:
                answer.append(False)
        return answer