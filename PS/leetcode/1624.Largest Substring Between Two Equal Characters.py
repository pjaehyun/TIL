class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        current = len(s) - 1
        for i in range(len(s) - 1, 0, -1):
            for j in range(len(s) - i):
                if s[j] == s[j + i]:
                    return i - 1
        return -1