class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(a, b):
            result = 1
            a %= MOD
            while b > 0:
                if b % 2 == 1:
                    result = (result * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return result

        even = (n + 1) // 2
        odd = n // 2
        return (power(5, even) * power(4, odd)) % MOD