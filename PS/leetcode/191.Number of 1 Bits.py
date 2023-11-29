# 첫번째 풀이
class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0
        answer = 0

        def devideAndConquer(num):
            nonlocal answer
            if num == 1:
                answer += 1
                return
            if num % 2 != 0:
                answer += 1
            devideAndConquer(num//2)
        devideAndConquer(n)
        return answer
    
# 두번째 풀이
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0

        while n != 0:
            answer += n%2
            n >>= 1
        return answer