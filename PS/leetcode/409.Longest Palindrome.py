class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        
        odd = 0

        for k, v in count.items():
            if v % 2 != 0:
                odd += 1
        
        return len(s) if odd <= 0 else len(s) + 1 - odd