class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set(arr)
        prev = set()

        prev.add(arr[0])
        for i in range(1, len(arr)):
            temp = set()
            for p in prev:
                temp.add(arr[i] | p)
                res.add(arr[i] | p)
            prev = temp
            prev.add(arr[i])
        return len(res)