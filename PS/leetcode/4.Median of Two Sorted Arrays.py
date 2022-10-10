class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        merge = sorted(nums1)
        if len(merge) % 2 == 0:
            mid1, mid2 = len(merge) // 2 - 1, len(merge) // 2
            print(mid1, mid2)
            return (merge[mid1] + merge[mid2]) / 2
        else:
            mid = len(merge) // 2
            return float(merge[mid])