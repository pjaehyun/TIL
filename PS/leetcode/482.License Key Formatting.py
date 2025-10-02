class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        answer = []
        
        temp = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "-": continue

            if len(temp) == k:
                answer.append(temp[::-1].upper())
                temp = ""
            temp += s[i]
        answer.append(temp[::-1].upper())
        
        return '-'.join(answer[::-1])