class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = max(len(word1), len(word2)), min(len(word1), len(word2))
        answer = []
        for i in range(m):
            answer.append(word1[i])
            answer.append(word2[i])
        return ''.join(answer) + word1[m:n] + word2[m:n]
            