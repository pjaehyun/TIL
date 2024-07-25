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
    
# 두번째 풀이
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr):
            if len(arr) < 2:
                return arr
            
            mid = len(arr) // 2
            low_arr = merge(arr[:mid])
            high_arr = merge(arr[mid:])

            l, h = 0, 0
            
            merge_sorted = []
            while l < len(low_arr) and h < len(high_arr):
                if low_arr[l] < high_arr[h]:
                    merge_sorted.append(low_arr[l])
                    l += 1
                else:
                    merge_sorted.append(high_arr[h])
                    h += 1
            
            merge_sorted += low_arr[l:]
            merge_sorted += high_arr[h:]
            return merge_sorted
        
        return merge(nums)
    
# 세번째 풀이
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)