class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}
        sorted_unique_numbers = sorted(list(set(arr)))
        
        for index in range(len(sorted_unique_numbers)): 
            value_to_rank[sorted_unique_numbers[index]] = index + 1
          
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]
        
        return arr