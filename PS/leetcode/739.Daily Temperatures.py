class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0 for _ in range(n)]
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return answer