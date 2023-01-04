class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        answer = 0
        for value in Counter(tasks).values():
            if value == 1:
                return -1
            elif (value - 2) % 3 == 0:
                answer += (value-2) // 3 + 1
            elif (value - 4) % 3 == 0:
                answer += (value-4) // 3 + 2
            elif value % 3 == 0:
                answer += value // 3
            else:
                answer += value // 2
        return answer
                
            