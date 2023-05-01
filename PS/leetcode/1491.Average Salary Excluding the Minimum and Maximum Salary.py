class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary)-2)