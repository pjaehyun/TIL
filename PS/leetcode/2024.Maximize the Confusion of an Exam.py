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
    
# 두번째 풀이(정답 참고)
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        t, f = 0, 0
        answer = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'F':
                f += 1
            else:
                t += 1
        
            while min(t, f) > k:
                if answerKey[l] == 'T':
                    t -= 1
                else:
                    f -= 1
                l += 1
            answer = max(answer, r - l + 1)
        return answer
        