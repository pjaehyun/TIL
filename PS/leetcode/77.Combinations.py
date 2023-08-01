class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = [x for x in range(1, n+1)]

        def backtracking(idx, comb):
            if len(comb) == k:
                answer.append(comb)
                return
            for i in range(idx+1, n):
                if lst[i] not in visited:
                    visited.add(lst[i])
                    backtracking(i, comb + [lst[i]])
                    visited.remove(lst[i])
        
        answer = []
        visited = set()
        for i in range(n):
            visited.add(lst[i])
            backtracking(i, [lst[i]])
        return answer