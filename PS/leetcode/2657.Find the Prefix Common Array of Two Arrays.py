class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        result = [0] * n
        count = [0] * (n + 1)
        common = 0
        
        for i in range(n):
            count[A[i]] += 1
            if count[A[i]] == 2:
                common += 1
            count[B[i]] += 1
            if count[B[i]] == 2:
                common += 1
            result[i] = common
        return result