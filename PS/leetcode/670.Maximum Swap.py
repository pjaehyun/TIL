class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        
        last = [0] * n
        last[-1] = n - 1 

        for i in range(n - 2, -1, -1):
            if num_str[i] > num_str[last[i + 1]]:
                last[i] = i
            else:
                last[i] = last[i + 1]

        for i in range(n):
            if num_str[i] != num_str[last[i]]:
                num_str[i], num_str[last[i]] = num_str[last[i]], num_str[i]
                return int(''.join(num_str))
        
        return num