class Solution:
    def countTriples(self, n: int) -> int:
        answer = 0
        
        for a in range(1, n+1):
            for b in range(1, n+1):
                cs = a**2 + b**2
                c = int(cs**0.5)
                if c**2 == cs and 1 <= c <= n:
                    answer += 1
        return answer

