# 첫번째 풀이
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        l = 1
        stack = []
        answer = []
        while stack != target:
            if not stack:
                stack.append(l)
                l += 1
                answer.append("Push")
            elif stack[-1] != target[len(stack) - 1]:
                stack.pop()
                answer.append("Pop")
            else:
                stack.append(l)
                l += 1
                answer.append("Push")
        return answer
    
# 두번째 풀이
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        answer = []
        idx = 0

        for i in range(1, n+1):
            answer.append("Push")
            if i == target[idx]:
                idx += 1
            else:
                answer.append("Pop")
            
            if idx == len(target):
                break
        return answer