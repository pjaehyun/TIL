class Solution:
    def isVowel(self, c: str) -> bool:
        return c in 'aeiou'
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        v = [1 if self.isVowel(word[0]) and self.isVowel(word[-1]) else 0 for word in words]
        pref = [0] * len(v)
        pref[0] = v[0]
        for i in range(1, len(v)):
            pref[i] = pref[i - 1] + v[i]
        
        ans = []
        for l, r in queries:
            ans.append(pref[r] if l == 0 else pref[r] - pref[l - 1])
        return ans