class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        stack = [-1]
        answer = 0

        for num in nums:
            while stack[-1] > num: stack.pop()

            if num > stack[-1]:
                if num > 0: answer += 1
                stack.append(num)
        return answer