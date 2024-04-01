class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len([c for c in s.split(' ') if c != ''][-1])