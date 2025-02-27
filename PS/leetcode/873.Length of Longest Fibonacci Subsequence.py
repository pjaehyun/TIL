class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        res = 0

        arr.sort()
        arr_dict = set(arr)

        for i in range(n):
            for j in range(i+1, n):
                l, r, t = arr[i], arr[j], 0
                while l + r in arr_dict:
                    t += 1
                    l, r = r, l+r
                res = max(res, t + 2)
        return res if res > 2 else 0