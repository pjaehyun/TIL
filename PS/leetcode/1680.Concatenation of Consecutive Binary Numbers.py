class Solution:
    def concatenatedBinary(self, n: int) -> int:
        arr = 1
        for i in range(2,n+1):
            arr = ((arr<<len(bin(i))-2) + i)%1000000007
        return arr