class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        roman = {'M':0,'CM':0,'D':0,'CD':0,'C':0,'XC':0,'L':0,'XL':0,'X':0,'IX':0,'V':0,'IV':0,'I':0}
        symbol = [('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)]
        
        for s in symbol:
            roman[s[0]] = num // s[1]
            num = num % s[1]

        for k, v in roman.items():
            for i in range(v):
                result += k
        return result
        