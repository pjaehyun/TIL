class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        r = mid - 1
            return -1

        def bs2():
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    if mid == len(nums) - 1 or nums[mid+1] != target:
                        return mid
                    else:
                        l = mid + 1
            return -1
        
        position1, position2 = bs(), bs2()
        return [position1, position2]
