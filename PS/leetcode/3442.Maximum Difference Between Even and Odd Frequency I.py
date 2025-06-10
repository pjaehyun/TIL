class Solution:
    def maxDifference(self, s: str) -> int:
        count = defaultdict(int)
        
        odd = 0
        even = float('inf')
        for c in s:
            count[c] += 1

        for v in count.values():
            if v % 2 == 0:
                even = min(even, v)
            else:
                odd = max(odd, v)
        return odd - even