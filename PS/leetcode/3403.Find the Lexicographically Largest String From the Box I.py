class Solution:
    def answerString(self, word: str, n: int) -> str:
        m=len(word)-n+1 
        if n==1: 
            return word
        return max(word[i:i+m] for i in range(len(word)))