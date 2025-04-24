class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        distinct_nums = len(set(nums))
        distinct_sub_nums = set()
        e = 1
        
        count = defaultdict(int)
        count[nums[0]] += 1
        distinct_sub_nums.add(nums[0])

        answer = 0
        for i in range(n):

            while e < n and not (distinct_nums == len(distinct_sub_nums)):
                count[nums[e]] += 1

                distinct_sub_nums.add(nums[e])
                e += 1

            if distinct_nums == len(distinct_sub_nums):
                answer += n - e + 1

            count[nums[i]] -= 1
            if count[nums[i]] <= 0:
                distinct_sub_nums.remove(nums[i])


        return answer