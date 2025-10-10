class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        answer = -1

        if len(a) < len(b):
            a, b = b, a

        for i in range(len(a)):
            for j in range(i+1, len(a)+1):
                if a[i:j] not in b:
                    answer = max(answer, len(a[i:j]))
        return answer