# 첫번째 풀이
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        i, j = 0, 0
        a = k
        answer = 0
        while j < len(answerKey):
            if answerKey[j] == 'T':
                j += 1
            elif answerKey[j] == 'F' and a > 0:
                j += 1
                a -= 1
            else:
                if answerKey[i] == 'F':
                    a += 1
                i += 1
            answer = max(answer, j - i)
        
        i, j = 0, 0
        a = k
        while j < len(answerKey):
            if answerKey[j] == 'F':
                j += 1
            elif answerKey[j] == 'T' and a > 0:
                j += 1
                a -= 1
            else:
                if answerKey[i] == 'T':
                    a += 1
                i += 1
            answer = max(answer, j - i)

        return answer