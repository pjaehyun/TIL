class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        dq = deque(target[1:])

        answer = target[0]
        prev = [target[0]]
        while dq:
            curr = dq.popleft()

            if curr > prev[-1]:
                answer += curr - prev[-1]
            prev.append(curr)
        return answer