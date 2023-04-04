# 첫번째 풀이
class Solution:
    def partitionString(self, s: str) -> int:
        
        i, j = 0, 1
        answer = 1
        while j < len(s):
            if s[j] in s[i:j]:
                i = j
                j += 1
                answer += 1
            else:
                j += 1
        return answer

# 두번째 풀이
class Solution:
    def partitionString(self, s: str) -> int:
        
        table = set()
        answer = 1

        for i in range(len(s)):
            if s[i] in table:
               table = set()
               answer += 1
            table.add(s[i])
        return answer