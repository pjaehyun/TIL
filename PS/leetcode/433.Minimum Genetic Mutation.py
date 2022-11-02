class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        def checkOneMutation(str1, str2):
            return sum([1 for i in range(len(str1)) if str1[i] != str2[i]]) == 1
            
        visited = set()
        visited.add(start)
        dq = deque([[start, 0]])
        
        while dq:
            current, mutation = dq.popleft()
            
            if current == end:
                return mutation
            
            for neighbor in bank:
                if checkOneMutation(current, neighbor) and neighbor not in visited:
                    visited.add(neighbor)
                    dq.append([neighbor, mutation + 1])
        return -1
