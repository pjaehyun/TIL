class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        answer = []
        counter = Counter(p)

        if len(p) > len(s):
            return []

        for i in range(len(p)-1):
            if s[i] in counter:
                counter[s[i]] -= 1
        for i in range(-1, len(s) - len(p) + 1):
            if i > -1 and s[i] in counter:
                counter[s[i]] += 1
            if i + len(p) < len(s) and s[i+len(p)] in counter:
                counter[s[i+len(p)]] -= 1
            if all(v == 0 for k, v in counter.items()):
                answer.append(i+1)
        return answer
