class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = str(bin(start))[2:]
        goal = str(bin(goal))[2:]
        
        if len(start) < len(goal):
            start, goal = goal, start
        
        goal = (len(start) - len(goal)) * '0' + goal
        
        answer = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                answer += 1
        return answer