class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        answer = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[left] + people[right] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            answer += 1
        return answer