class Solution:
    def passThePillow(self, n: int, time: int) -> int:
         chunks = time // (n - 1)
         return (time % (n - 1) + 1) if chunks % 2 == 0 else (n - time % (n - 1))