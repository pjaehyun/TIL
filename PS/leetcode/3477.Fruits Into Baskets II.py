class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        
        alloc = 0
        for i in range(n):
            for j in range(n):
                if baskets[j] != -1 and fruits[i] <= baskets[j]:
                    baskets[j] = -1
                    alloc += 1
                    break
        return n - alloc