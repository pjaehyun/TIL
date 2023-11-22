# 첫번째 풀이 
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonal[i+j].append(nums[i][j])
        answer = []
        for k, v in diagonal.items():
            v = reversed(v)
            answer.extend(v)
        return answer
    
# 두번째 풀이
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dq = deque()

        answer = []

        dq.append((0, 0))

        while dq:
            x, y = dq.popleft()

            answer.append(nums[x][y])

            if x + 1 < len(nums) and y == 0:
                dq.append((x+1, y))
            
            if y + 1 < len(nums[x]):
                dq.append((x, y+1))
        return answer