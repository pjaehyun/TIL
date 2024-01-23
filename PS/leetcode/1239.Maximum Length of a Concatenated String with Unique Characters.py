# 첫번째 풀이
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

# 두번째 풀이
class Solution:
    def maxLength(self, arr: List[str]) -> int:
         answer = ""

         def unique (s):
             comp = defaultdict(int)

             for i in range(len(s)):
                 if comp[s[i]] >= 1:
                     return False
                 comp[s[i]] += 1
             return True

         def bt(i, concat):
             nonlocal answer 
             if len(concat) > len(answer):
                 answer = concat
            
             for j in range(i+1, len(arr)):
                 if j not in visited and unique(concat + arr[j]):
                     visited.add(j)
                     bt(j, concat + arr[j])
                     visited.remove(j)
        
         visited = set()

         for i in range(len(arr)):
             if unique(arr[i]):
                visited.add(i)
                bt(i, arr[i])
                visited.remove(i)
         return len(answer)

        