class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        count = Counter(s)
        
        even = 0
        odd = 0

        for _, v in count.items():
            even += v // 2
            odd += v % 2
        if odd > k or odd + (even*2) < k:
            return False
        return True