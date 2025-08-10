class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(num):
            counts = [0] * 10
            if num == 0:
                counts[0] = 1
                return tuple(counts)
            
            while num > 0:
                counts[num % 10] += 1
                num //= 10
            return tuple(counts)

        n_counts = count_digits(n)

        for i in range(30): 
            power_of_two = 1 << i  
            if count_digits(power_of_two) == n_counts:
                return True
        
        return False