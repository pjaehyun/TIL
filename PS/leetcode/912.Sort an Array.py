class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left, right):
            res = []

            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
            if i == len(left):
                res += right[j:]
            else:
                res += left[i:]
            return res
        
        def devide(lst):
            if len(lst) < 2:
                return lst
            mid = len(lst) // 2
            left, right = devide(lst[:mid]), devide(lst[mid:])
            return merge(left, right)

        return devide(nums)