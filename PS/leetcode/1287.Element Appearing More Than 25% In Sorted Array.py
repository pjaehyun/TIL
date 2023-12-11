class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        prev = 0
        prev_len = 1
        answer = arr[0]
        for i in range(1, n):
            if arr[prev] != arr[i]:
                if i - prev > prev_len:
                    answer = arr[prev]
                    prev_len = i - prev
                prev = i
        if n - prev > prev_len:
            answer = arr[prev]
        return answer