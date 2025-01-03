class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref=[nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[i-1]+nums[i])
        res=0
        for i in range(len(pref)-1):
            if pref[i]>=pref[-1]-pref[i]:
                res+=1
        return res