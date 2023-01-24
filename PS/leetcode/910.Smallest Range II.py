class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        answer = nums[-1] - nums[0]
        for i in range(len(nums) - 1):
            # 가장 차이가 큰 값
            # nums[-1]: nums[i]와 nums[-1]에 둘다 k를 더하거나 뺏을경우
            # nums[i]+2*K: nums[i] - k 와 nums[-1] + k의 차이
            _max = max(nums[-1], nums[i]+2*k) 

             # 가장 차이가 작은 값 
             # nums[i+1]: nums[i+1]과 nums[0]에 둘다 k를 더하거나 뺏을경우
             # nums[0]+2*k: nums[0] - k 와 nums[i+1] + k의 차이
            _min = min(nums[i+1], nums[0]+2*k)
            answer = min(answer, _max-_min)

        return answer