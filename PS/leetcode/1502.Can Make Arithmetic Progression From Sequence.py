class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()

        diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            temp = arr[i] - arr[i-1]
            if temp != diff:
                return False
        return True