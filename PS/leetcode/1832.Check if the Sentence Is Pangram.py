# 첫번째 풀이
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        for a in alphabet:
            if a not in sentence:
                return False
        return True


# 두번째 풀이
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26