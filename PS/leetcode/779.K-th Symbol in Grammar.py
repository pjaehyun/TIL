# Not연산을 이용한다는 것은 알았지만 구현하지 못하여 다른 풀이 참고
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        prevLength = 2**(n-2)

        if k <= prevLength:
            return self.kthGrammar(n-1, k)
        else:
            return 1 - self.kthGrammar(n-1, k-prevLength)