class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = int(''.join([str(x) for x in num]))
        
        temp = str(num + k)

        answer = [int(x) for x in temp]
        return answer
        