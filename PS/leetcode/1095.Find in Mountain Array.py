# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def get_top():
            l, r = 0, mountain_arr.length() - 1
            while l < r:
                mid = (l + r) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def bs_left(start, end, target):
            
            while start <= end:
                mid = (start + end) // 2
                temp = mountain_arr.get(mid)
                if temp == target:
                    return mid

                if mountain_arr.get(mid) < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        
        def bs_right(start, end, target):
            while start <= end:
                mid = (start + end) // 2
                temp = mountain_arr.get(mid)
                if temp == target:
                    return mid

                if mountain_arr.get(mid) < target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        top_idx = get_top()
        uphill = bs_left(0, top_idx, target)
        if uphill >= 0:
            return uphill
        else:
            return bs_right(top_idx, mountain_arr.length() -1, target)