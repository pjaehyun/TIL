# 첫번째 풀이
class Solution:
    def addDigits(self, num: int) -> int:
        
        num = str(num)
        while len(num) != 1:
            total = 0
            for i in range(len(num)):
                total += int(num[i])
            num = str(total)
        return int(num)

# 두번째 풀이(루프 없이 풀이)
class Solution:
    def addDigits(self, num: int) -> int:
        
        if num == 0:
            return 0
        
        if num % 9 == 0:
            return 9
        else:
            return num % 9