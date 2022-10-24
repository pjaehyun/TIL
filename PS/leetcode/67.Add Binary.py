class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        if len(a) - len(b) > 0:
            b = "0" * (len(a) - len(b)) + b
        else:
            a = "0" * (len(b) - len(a)) + a
        
        for i in range(len(a) - 1, -1, -1):
            x, y = int(a[i]), int(b[i])
            if (x + y + carry) == 0:
                result += '0'
                carry = 0
            elif (x + y + carry) == 1:
                result += '1'
                carry = 0
            elif (x + y + carry) == 2:
                result += '0'
                carry = 1
            elif (x + y + carry) == 3:
                result += '1'
                carry = 1
        if carry == 1:
            result += '1'
        return result[::-1]