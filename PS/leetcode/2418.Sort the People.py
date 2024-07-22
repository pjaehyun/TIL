class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [n for n, h in sorted([(n, h) for n, h in zip(names, heights)], key=lambda x:(x[1], x[0]), reverse=True)]