class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack, answer = [], [0] * len(arr)
        
        for i, n in enumerate(arr):
            while stack and arr[stack[-1]] > n:
                stack.pop()
            j = stack[-1] if stack else -1
            answer[i] = answer[j] + (i - j) * n
            stack.append(i)
        return sum(answer) % 1000000007