class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(column) != sorted(column) for column in zip(*strs))
