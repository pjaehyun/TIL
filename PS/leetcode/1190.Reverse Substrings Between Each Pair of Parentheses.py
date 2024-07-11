class Solution:
    def reverseParentheses(self, s: str) -> str:
        answer = []

        for i in range(len(s)):
            if s[i] == ")":
                temp = ""
                while answer and answer[-1] != "(":
                    temp += answer.pop()
                answer.pop()
                
                answer += list(temp)
            else:    
                answer.append(s[i])
        return ''.join(answer)