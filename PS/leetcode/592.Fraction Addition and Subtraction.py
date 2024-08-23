import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall('[+-]?\\d+/\\d+', expression)
        
        numerator = 0
        denominator = 1
        
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            
            numerator = numerator * denom + num * denominator
            denominator *= denom
        
        common_divisor = gcd(abs(numerator), denominator)
        
        numerator //= common_divisor
        denominator //= common_divisor
        
        return f"{numerator}/{denominator}"
