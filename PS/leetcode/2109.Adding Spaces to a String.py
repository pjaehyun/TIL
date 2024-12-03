class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""

        prev_idx = 0
        for space in spaces:
            answer += s[prev_idx:space] + " "
            prev_idx = space
        return answer + s[prev_idx:]