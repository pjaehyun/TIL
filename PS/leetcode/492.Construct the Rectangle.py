class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        answer = [area, 1]

        for i in range(1, area//2+1):
            if area % i == 0:
                x,y=i,area//i
                if x >= y and abs(answer[0] - answer[1]) >= abs(x-y):
                    answer = [x,y]
        return answer
        