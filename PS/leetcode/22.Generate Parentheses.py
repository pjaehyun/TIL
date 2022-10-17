# 재귀를 이용한 문제풀이
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(par, left, right):
            if left == 0 and right == 0: result.append(par)
            if left: dfs(par+'(', left - 1, right)
            if right > left: dfs(par+')',left,right-1)
        
        dfs('(',n-1,n)
        return result


# Stack을 이용한 문제풀이
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [('(',n-1,n)]

        while stack:
            items = stack.pop(0)

            if items[1] == 0 and items[2] == 0:
                result.append(items[0])
            if items[1]: stack.append((items[0]+'(',items[1]-1,items[2]))
            if items[2] > items[1]: stack.append((items[0]+')',items[1],items[2]-1))
        return result