class Solution:
    def makeFancyString(self, s: str) -> str:
        prev = s[0]
        cons = 1
        answer = s[0]
        for i in range(1, len(s)):
            if s[i] == prev:
                if cons >= 2:
                    continue
                answer += s[i]
                cons += 1
            else:
                answer += s[i]
                prev = s[i]
                cons = 1
        return answer