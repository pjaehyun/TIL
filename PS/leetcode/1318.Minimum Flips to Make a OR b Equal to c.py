class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:        
        answer = 0

        while a > 0 or b > 0 or c > 0:
            b_a = a & 1
            b_b = b & 1
            b_c = c & 1

            if b_c == 0:
                answer += (b_a + b_b)
            else:
                if b_a == 0 and b_b == 0:
                    answer += 1

            a >>= 1
            b >>= 1
            c >>= 1
        return answer