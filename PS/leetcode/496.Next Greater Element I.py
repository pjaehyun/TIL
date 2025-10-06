class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        idxs = {nums2[i]:i for i in range(len(nums2))}
        
        answer = [-1] * len(nums1)
        for i in range(len(nums1)):
            greater = -1
            for j in range(idxs[nums1[i]]+1, len(nums2)):
                if nums1[i] < nums2[j]:
                    greater = nums2[j]
                    break
            answer[i] = greater
        return answer