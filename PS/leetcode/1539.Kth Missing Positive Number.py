# 첫번째 풀이
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lst = [x for x in range(1, 10001)]
        
        for num in arr:
            lst.remove(num)
        return lst[k-1]

# 두번째 풀이(이진탐색)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            v = arr[mid] - mid - 1
            if v >= k:
                right = mid - 1
            else:
                left = mid + 1
        return k + left