# 첫번째 풀이
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        
        for key, value in t_count.items():
            if s_count[key] != value:
                return key
            
# 두번째 풀이(다른 풀이 참고)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:  
        c = 0
        for cs in s: c ^= ord(cs)
        for ct in t: c ^= ord(ct)
        return chr(c)