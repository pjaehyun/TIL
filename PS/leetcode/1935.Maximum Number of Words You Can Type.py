class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        answer = len(words)
        for word in words:
            for c in word:
                if c in brokenLetters:
                    answer -= 1
                    break
        return answer