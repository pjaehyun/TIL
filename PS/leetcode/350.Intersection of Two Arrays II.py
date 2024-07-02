class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        nums2_count = Counter(nums2)

        answer = []

        for k, v in nums1_count.items():
            if k in nums2_count:
                answer += [k] * min(v, nums2_count[k])
        return answer