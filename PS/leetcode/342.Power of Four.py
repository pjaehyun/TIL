# brute force
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        while n > 1:
            if n % 4 == 0:
                n //= 4
            else:
                break
        return n == 1
    
# recursion
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        def recursion(num):
            if num % 4 == 0:
                return recursion(num // 4)
            else:
                return num
        if n == 0:
            return False
        return recursion(n) == 1

# math(다른 풀이 참고)
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n <= 0:
            return False
        
        sqrt = math.sqrt(n)

        log2 = math.log2(sqrt)
        return log2 == int(log2)