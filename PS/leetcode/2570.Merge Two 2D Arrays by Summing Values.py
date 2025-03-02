class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        nums = defaultdict(int)

        n, m = len(nums1), len(nums2)

        for i in range(n):
            nums[nums1[i][0]] += nums1[i][1]
        
        for i in range(m):
            nums[nums2[i][0]] += nums2[i][1]
        
        answer = []

        for k, v in nums.items():
            answer.append([k, v])
        answer.sort()
        return answer