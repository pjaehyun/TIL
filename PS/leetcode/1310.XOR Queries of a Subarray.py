class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * n
        ans = []

        prefix[0] = arr[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] ^ arr[i]

        for left, right in queries:
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append(prefix[right] ^ prefix[left - 1])

        return ans
