class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_set=0
        for b in range(24):
            b_bit_set=0
            for x in candidates:
                b_bit_set+=(x>>b &1)
            max_set=max(max_set, b_bit_set)
        return max_set