class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        
        n = len(spells)
        m = len(potions)

        answer = []
        for i in range(n):
            pairs = 0
            left, right = 0, m-1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spells[i] < success:
                    left = mid + 1
                else:
                    right = mid - 1
            answer.append(m-left)

        return answer
