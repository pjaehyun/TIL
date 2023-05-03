class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = []
        nums1 = set(nums1)
        nums2 = set(nums2)

        answer.append([x for x in nums1 if x not in nums2])
        answer.append([x for x in nums2 if x not in nums1])
        return answer