class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = 0
        for word in words:
            check = True
            for c in word:
                if c not in allowed:
                    check = False
                    break
            if check:
                answer += 1
        return answer