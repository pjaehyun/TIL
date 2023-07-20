class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]
        
        for i in range(1, len(asteroids)):
            while stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack[-1] < abs(asteroids[i]):
                    stack.pop()
                elif stack[-1] + asteroids[i] == 0:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroids[i])

        return stack