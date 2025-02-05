class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        s1_count = Counter(s1)

        swap = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]: swap += 1
            s1_count[s2[i]] -= 1
        
        for k, v in s1_count.items():
            if v != 0:
                return False
        return True if swap <= 2 else False