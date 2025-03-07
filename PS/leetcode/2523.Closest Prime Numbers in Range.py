class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [i for i in range(right+1)]
        primes[1] = 0

        n = int(right**0.5)
        for i in range(2, n+1):
            if primes[i] == 0: continue

            for j in range(i*i, right+1, i):
                primes[j] = 0
        
        primes = sorted([x for x in primes if x >= left])
        if len(primes) < 2:
            return [-1, -1]
        diff = primes[1] - primes[0]
        answer = [primes[0], primes[1]]
        for i in range(2, len(primes)):
            if primes[i] - primes[i-1] < diff:
                answer = [primes[i-1], primes[i]]
                diff = primes[i] - primes[i-1]
        return answer
                
        