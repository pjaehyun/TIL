class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        lst = sorted(set(nums))
        lst_dict = {}
        for i in range(len(lst)):
            lst_dict[lst[i]] = i

        answer = 0
        for i in range(len(nums)):
            answer += lst_dict[nums[i]]
        return answer