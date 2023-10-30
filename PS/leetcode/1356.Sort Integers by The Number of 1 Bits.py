# 첫번째 풀이
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return [num for num, count in sorted([(x, int(bin(x).count('1'))) for x in arr], key=lambda x:(x[1], x[0]))]
    
# 두번째 풀이
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_one(num):
            
            count = 0
            while num:
                count += 1
                num &= (num-1)
            return count
        
        arr.sort(key = lambda x: (count_one(x), x))
        return arr