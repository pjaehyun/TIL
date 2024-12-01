class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i == j: continue

                if arr[i] == arr[j]*2:
                    return True
        return False