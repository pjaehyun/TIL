class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return "0"

        minus = num < 0
        num = abs(num)
        temp = ""
        while num > 0:
            curr=num%7
            temp+=str(curr)
            num//=7
        if minus: return '-' + temp[::-1]
        return temp[::-1]
        