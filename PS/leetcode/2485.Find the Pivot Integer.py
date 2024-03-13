class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + i
        
        for i in range(n+1):
            if prefix_sum[-1] - prefix_sum[i] + i == prefix_sum[i]:
                return i
        return -1