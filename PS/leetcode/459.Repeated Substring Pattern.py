# 첫번째 풀이
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            temp = s[:i]
            if temp * (len(s) // i) == s:
                return True
        return False

# 두번째 풀이
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]    