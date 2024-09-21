class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(curr):
            if curr > n:
                return
            answer.append(curr)

            for i in range(10):
                if curr * 10 + i > n:
                    return
                dfs(curr*10+i)
                
        answer = []

        for i in range(1, 10):
            dfs(i)
        
        return answer