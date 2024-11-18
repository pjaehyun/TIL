class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        def next():
            res = []
            for i in range(n):
                _sum = 0
                for j in range(i+1, i+k+1):
                    _sum += code[j%n]
                res.append(_sum)
            return res

        def previous():
            res = []
            for i in range(n):
                _sum = 0
                for j in range(i-1, i+k-1, -1):
                    _sum += code[j%n]
                res.append(_sum)
            return res

        if k > 0:
            return next()
        if k < 0:
            return previous()
        if k == 0:
            return [0] * n