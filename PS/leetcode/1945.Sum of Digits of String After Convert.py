class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ""
        for c in s:
            convert += str(ord(c) - ord('a') + 1)
        
        for i in range(k):
            temp = 0
            for c in convert:
                temp += int(c)
            convert = str(temp)
        return int(convert)