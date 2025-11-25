class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1 
        
        rem = 1 % k

        len = 1

        while rem > 0:
            rem = (rem * 10 + 1) % k 
            len += 1
            if len > k:
                return -1
        return len