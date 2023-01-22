class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []

        def backtracking(sub, idx):
            if idx == len(s):
                answer.append(sub[:])
            temp = ""
            for i in range(idx, len(s)):
                temp = temp + s[i]
                if temp == temp[::-1]:
                    sub.append(temp)
                    backtracking(sub, i+1)
                    sub.pop()

        
        backtracking([], 0)
        return answer