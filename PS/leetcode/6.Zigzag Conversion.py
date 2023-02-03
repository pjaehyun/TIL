class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = ["" for _ in range(numRows)]
        
        between = numRows - 2

        if len(s) <= numRows or numRows == 1:
            return s
        
        zigzag = numRows + between
        for i in range(numRows):
            temp = i
            while temp < len(s):
                answer[i] += s[temp]
                if 0 < i < numRows - 1 and temp+zigzag < len(s):
                    answer[i] += s[temp+zigzag]
                temp += numRows + between
            zigzag -= 2
        return ''.join(answer)
        