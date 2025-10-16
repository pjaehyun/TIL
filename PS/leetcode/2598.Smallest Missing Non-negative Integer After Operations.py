class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod = [0] * value
        for num in nums:
            num = (num % value + value) % value
            mod[num]+=1
        
        res = 0
        while mod[res % value]:
            mod[res % value] -= 1
            res += 1
        return res