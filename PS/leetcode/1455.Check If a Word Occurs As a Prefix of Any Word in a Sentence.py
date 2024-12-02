class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        split_sentence = sentence.split(' ')
        for i in range(len(split_sentence)):
            if len(split_sentence[i]) < len(searchWord):
                continue
            else:
                if split_sentence[i][:len(searchWord)] == searchWord:
                    return i + 1
        return -1