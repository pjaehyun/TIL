class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        answer = 0
        for i in range(len(nums)):
            inc_temp = nums[i]
            inc_max_len = 1
            for j in range(i+1, len(nums)):
                if nums[j] > inc_temp:
                    inc_temp = nums[j]
                    inc_max_len += 1
                else: break
            answer = max(answer, inc_max_len)

        for i in range(len(nums)):
            dec_temp = nums[i]
            dec_max_len = 1
            for j in range(i+1, len(nums)):
                if nums[j] < dec_temp:
                    dec_temp = nums[j]
                    dec_max_len += 1
                else: break
            answer = max(answer, dec_max_len)
        return answer