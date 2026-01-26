class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        diff = []
        for i in range(1, len(arr)):
            diff.append([arr[i-1], arr[i], abs(arr[i-1] - arr[i])])
        
        diff.sort(key=lambda x:x[2])
        
        mad = diff[0][2]

        answer = []
        for i in range(len(diff)):
            if diff[i][2] == mad:
                answer.append([diff[i][0], diff[i][1]])
            else:
                break
        return answer