class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        
        answer = []
        
        for el in arr2:
            for _ in range(count[el]):
                answer.append(el)
            del count[el]
        
        temp = sorted((k, v) for k, v in count.items())
        
        for i in range(len(temp)):
            for _ in range(temp[i][1]):
                answer.append(temp[i][0])

        return answer