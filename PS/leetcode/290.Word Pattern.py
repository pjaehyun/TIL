# 첫번째 풀이
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp = s.split()
        
        if len(temp) != len(pattern):
            return False
        ht = {}
        seen = set()
        for i in range(len(pattern)):
            if pattern[i] not in ht:
                if temp[i] in seen:
                    return False
                ht[pattern[i]] = temp[i]
                seen.add(temp[i])
            else:
                if ht[pattern[i]] != temp[i]:
                    return False
        return True
                
# 두번째 풀이 (set 안쓰고 딕셔너리로만 풀이)
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        temp = s.split()
        if len(temp) != len(pattern): return False
        ht = {}
        seen = {}
        for i in range(len(pattern)):
            if pattern[i] not in ht and temp[i] not in seen:
                ht[pattern[i]] = temp[i]
                seen[temp[i]] = pattern[i]

        answer = ""
        for i in range(len(pattern)):
            if temp[i] in seen:
                answer += seen[temp[i]]
                
        return answer == pattern