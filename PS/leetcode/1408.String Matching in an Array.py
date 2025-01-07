class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        answer = []
        for i in range(n):
            for j in range(n):
                if i == j: continue

                if words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer