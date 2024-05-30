class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        
        answer = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                
                a = 0
                for k in range(i, j):
                    a ^= arr[k]
                
                b = 0
                for k in range(j, len(arr)):
                    b ^= arr[k]
                    if a == b:
                        answer += 1
        return answer