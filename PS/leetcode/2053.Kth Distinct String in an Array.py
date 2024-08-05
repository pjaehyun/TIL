class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        distinct = 0

        for a in arr:
            if count[a] == 1:
                distinct += 1
            if distinct == k:
                return a
        return ""