class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        if n % 2 == 0 and m % 2 == 0:
            return 0

        nums1_xor = 0
        for i in range(n):
            nums1_xor ^= nums1[i]
        nums2_xor = 0
        for i in range(m):
            nums2_xor ^= nums2[i]
        
        if m % 2 == 0:
            return nums2_xor
        
        if n % 2 == 0:
            return nums1_xor
        
        return nums1_xor^nums2_xor
        
