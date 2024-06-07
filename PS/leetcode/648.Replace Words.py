class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence_split = sentence.split(' ')

        answer = []
        
        for word in sentence_split:
            find = False
            for i in range(1, len(word)):
                if word[:i] in dictionary:
                    answer.append(word[:i])
                    find = True
                    break
            if not find:
                answer.append(word)
        return ' '.join(answer)