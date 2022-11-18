# 첫번째 풀이
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        devisor = get_devisor(n)
        for d in devisor:
            res = is_prime(d)
            if res:
                if d != 2 and d != 3 and d != 5:
                    return False
        return True
            

def get_devisor(n):
    result = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            result.append(i)
            if i ** 2 != n:
                result.append(n // i)
    return result

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True

# 두번째 풀이(시간복잡도 개선)
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for i in [2,3,5]:
            while n % i == 0:
                n = n // i
        return n==1