class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10**9 + 7

        countA = 1
        countE = 1
        countI = 1
        countO = 1
        countU = 1

        for _ in range(1, n):
            countA = countE
            nextCountE = (countA + countI) % mod
            nextCountI = (countA + countE + countO + countU) % mod
            nextCountO = (countI + countU) % mod
            nextCountU = countA

            countA = nextCountA
            countE = nextCountE
            countI = nextCountI
            countO = nextCountO
            countU = nextCountU

        return (countA + countE + countI + countO + countU) % mod
        