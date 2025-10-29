class Solution:
    def smallestNumber(self, n: int) -> int:
        
        def br(x):
            answer = []
            while x > 0:
                m = x % 2
                if m == 0: return False
                x = x // 2
                answer.append(m)
            return True
        
        for i in range(n, 10000):
            if br(i): return i
        
        