class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        
        divided = 0
        not_divided = 0

        for i in range(1, n+1):
            if i % m == 0:
                divided += i
            else:
                not_divided += i
        return not_divided - divided