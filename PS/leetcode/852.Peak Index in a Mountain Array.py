class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j = 0, len(arr) - 1

        while i < j:
            if arr[i] < arr[i+1]:
                i += 1
            
            if arr[j] < arr[j-1]:
                j -= 1
        return i