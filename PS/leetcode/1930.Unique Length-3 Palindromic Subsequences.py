class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        answer = 0

        for k in string.ascii_lowercase:
            first, last = s.find(k), s.rfind(k)
            if first > -1:
                answer += len(set(s[first + 1:last]))
        return answer