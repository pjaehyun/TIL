# 첫번째 풀이
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sorted(list((k, v) for k, v in Counter(nums).items()), key=lambda x:x[1])[0][0]

# 두번째 풀이(이진탐색)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid+1]:
                low += 2
            else:
                high = mid
        print(nums[low])