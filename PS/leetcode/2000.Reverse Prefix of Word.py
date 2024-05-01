class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                temp = word[:i+1]
                temp = temp[::-1]
                return temp + word[i+1:]
        return word