class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        from sortedcontainers import SortedList
        counter = collections.Counter(nums[:k])
        sorted_counter = SortedList((-j, -i) for i, j in counter.items())
        prev_sum = sum(i * j for i, j in sorted_counter[:x])
        res = []
        for i in range(len(nums)-k + 1):
            res.append(prev_sum)
            if i == len(nums)-k:
                break
            out = (-counter[nums[i]], -nums[i])
            counter[nums[i]] -= 1
            out_idx = sorted_counter.bisect_left(out)
            if out_idx < x:
                prev_sum -= out[0] * out[1]
            sorted_counter.remove(out)
            if out_idx < x and len(sorted_counter) >= x:
                prev_sum += sorted_counter[x-1][0] * sorted_counter[x-1][1]
            
            if counter[nums[i]] != 0:
                in1 = (-counter[nums[i]], -nums[i])
                in1_idx = sorted_counter.bisect_left(in1)
                if in1_idx < x:
                    if len(sorted_counter) >= x:
                        prev_sum -= sorted_counter[x-1][0] * sorted_counter[x-1][1]
                    prev_sum += in1[0] * in1[1]
                sorted_counter.add(in1)
                
            if counter[nums[i+k]] != 0:
                out2 = (-counter[nums[i+k]], -nums[i+k])
                out2_idx = sorted_counter.bisect_left(out2)
                if out2_idx < x:
                    prev_sum -= out2[0] * out2[1]
                sorted_counter.remove(out2)
                if out2_idx < x and len(sorted_counter) >= x:
                    prev_sum += sorted_counter[x-1][0] * sorted_counter[x-1][1]
                    
            counter[nums[i+k]] += 1
            in2 = (-counter[nums[i+k]], -nums[i+k])
            in2_idx = sorted_counter.bisect_left(in2)
            if in2_idx < x:
                if len(sorted_counter) >= x:
                    prev_sum -= sorted_counter[x-1][0] * sorted_counter[x-1][1]
                prev_sum += in2[0] * in2[1]
            sorted_counter.add(in2)
        return res