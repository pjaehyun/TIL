class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        curr = 0
        n = len(nums)
        
        maximized = 2**maximumBit-1
        answer = []
        for i in range(n):
            curr ^= nums[i]
        answer.append(curr^maximized)
        for i in range(n-1, 0, -1):
            curr ^= nums[i]
            answer.append(curr^maximized)
        return answer
        