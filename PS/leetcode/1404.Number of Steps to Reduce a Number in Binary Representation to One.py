class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        sq = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                num += 2**sq
            sq += 1
        answer = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num + 1
            answer += 1
        return answer