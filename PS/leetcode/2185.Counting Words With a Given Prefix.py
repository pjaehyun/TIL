class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for word in words:
            if len(word) >= len(pref) and pref == word[:len(pref)]:
                answer += 1
        return answer