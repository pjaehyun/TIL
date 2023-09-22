# 첫번째 풀이
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        i = 0
        answer = ""
        for char in s:
            while i < len(t) and t[i] != char:
                i += 1
                
            if i < len(t) and char == t[i]:
                answer += t[i]
            i += 1

        return answer == s

# 두번째 풀이(코드 개선)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        return i == len(s)