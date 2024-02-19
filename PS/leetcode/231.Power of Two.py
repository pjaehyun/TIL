# 첫번째 풀이
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        def recursion(n):
            if n == 1:
                return True
            
            if n % 2 == 0:
                return recursion(n//2)
            return False
        return recursion(n)
    
# 두번째 풀이
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)