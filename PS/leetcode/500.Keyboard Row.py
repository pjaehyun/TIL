class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = {}
        
        for f in "qwertyuiopQWERTYUIOP":
            rows[f] = 'F'
        for s in "asdfghjklASDFGHJKL":
            rows[s] = "S"
        for t in "zxcvbnmZXCVBNM":
            rows[t] = "T"
        
        answer = []
        for word in words:
            c = word[0]
            same = True
            for i in range(1, len(word)):
                if rows[c] != rows[word[i]]:
                    same=False
                    break
            if same:
                answer.append(word)

        return answer