class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = Counter(nums)

        i_count = defaultdict(int)
        i_count[nums[0]] += 1

        answer = 0
        for j in range(1, n-1):
            temp = nums[j] * 2
            count[nums[j]] -= 1

            answer += (count[temp] - i_count[temp]) * i_count[temp]

            count[nums[j]] += 1
            i_count[nums[j]] += 1
        return answer % (10**9 + 7)