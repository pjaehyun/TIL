class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        p = 15
        
        answer = 0
        temp = n
        while p >= 0:
            if 3**p <= temp:
                answer += 3**p
                temp -= 3**p
            p -= 1
        return True if answer == n else False