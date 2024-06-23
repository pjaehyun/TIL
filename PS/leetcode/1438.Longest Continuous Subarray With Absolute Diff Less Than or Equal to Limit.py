class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        increase = deque()
        decrease = deque()
        max_length = 0
        left = 0

        for right in range(len(nums)):
            while increase and nums[right] < increase[-1]:
                increase.pop()
            increase.append(nums[right])
            
            while decrease and nums[right] > decrease[-1]:
                decrease.pop()
            decrease.append(nums[right])
            
            while decrease[0] - increase[0] > limit:
                if nums[left] == increase[0]:
                    increase.popleft()
                if nums[left] == decrease[0]:
                    decrease.popleft()
                left += 1
                
            max_length = max(max_length, right - left + 1)
        
        return max_length