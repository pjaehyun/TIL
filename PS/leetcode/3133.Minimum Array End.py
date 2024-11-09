class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n_1, ans, j=n-1, 0, 0
        for i in range(56):
            if (x>>i)&1: 
                ans|=(1<<i)
            else:
                if (n_1>>j)&1: ans|=(1<<i)
                j+=1
        return ans