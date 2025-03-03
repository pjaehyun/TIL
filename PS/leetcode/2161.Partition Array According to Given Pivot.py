class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        m = []
        r = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                l.append(nums[i])
            elif nums[i] > pivot:
                r.append(nums[i])
            else:
                m.append(nums[i])
        return l + m + r
