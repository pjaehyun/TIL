class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i, j = 0, len(letters) - 1
        while i <= j:
            mid = (i + j) // 2
            if letters[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return letters[0] if i >= len(letters) else letters[i]