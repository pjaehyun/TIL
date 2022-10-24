class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [""]
        for i in range(len(arr)):
            if len(arr[i]) > len(set(arr[i])): continue
            for j in range(len(result)):
                temp = result[j] + arr[i]
                if len(temp) == len(set(temp)):
                    result.append(temp)
        result.sort(key=lambda x:len(x))
        return len(result[-1])