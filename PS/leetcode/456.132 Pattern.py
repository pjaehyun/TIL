class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        last = float('-inf')
        
        for num in reversed(nums):
            if num < last:
                return True
            
            while stack and num > stack[-1]:
                last = stack.pop()
            stack.append(num)
        return False
