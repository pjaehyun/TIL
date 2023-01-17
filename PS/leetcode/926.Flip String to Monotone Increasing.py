class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, answer = 0, 0

        for num in s:
            if num == '1': ones += 1
            elif ones > 0:
                ones -= 1
                answer += 1
        return answer