class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([''.join(reversed(list(x))) for x in s.split(' ')])