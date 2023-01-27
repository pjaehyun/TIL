class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def check(word, words):
            for i in range(1, len(word)):
                lw = word[:i]
                rw = word[i:]
                if lw in words and (rw in words or check(rw,words)):
                    return True
            return False

        word_set = set()
        answer = []

        for w in words:
            word_set.add(w)
        
        for w in words:
            if check(w, word_set):
                answer.append(w)
        return answer