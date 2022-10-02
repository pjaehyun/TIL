class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        result = [0 for _ in range(len(s))]
        idx = 0
        s = list(s)
        while s:
            char = s.pop(0)
            lst = [char]
            for i in range(len(s)):
                if char == s[i] or s[i] in lst:
                    break
                lst.append(s[i])
            result[idx] = len(lst)
            idx += 1
        return max(result)