class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        counter = Counter(s1)
        n = len(s1)

        for i in range(len(s2)):
            if s2[i] in counter:
                counter[s2[i]] -= 1
            
            if i >= n and s2[i-n] in counter:
                counter[s2[i-n]] += 1
            
            check = True
            for k, v in counter.items():
                if v != 0:
                    check = False
                    break
            if check:
                return True
        return False
                