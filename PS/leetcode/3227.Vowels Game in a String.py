class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if (0x104111 >> (ord(c) - 97)) & 1:
                return True
        return False