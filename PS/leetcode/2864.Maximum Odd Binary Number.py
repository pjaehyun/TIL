class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count('1')
        zero_count = s.count('0')
        return '1' * (one_count - 1) + '0' * zero_count + '1'
