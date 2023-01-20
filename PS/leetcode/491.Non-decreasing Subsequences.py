# 첫번째 풀이(시간복잡도 겨우 통과)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []

        def backtracking(nums, idx):
            visited = set()
            if len(path) > 1:
                answer.append(path[:])
            
            for i in range(idx, len(nums)):
                if nums[i] in visited:
                    continue
                if path and path[-1] > nums[i]:
                    continue
                visited.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()

        backtracking(nums, 0)
        return answer

# 두번째 풀이(시간복잡도 개선)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []

        def backtracking(nums, idx):
            visited = set()
            if len(path) > 1:
                answer.append(path[:])
            
            for i in range(idx, len(nums)):
                if nums[i] in visited:
                    continue
                if path and path[-1] > nums[i]:
                    continue
                # visited를 사용하지 않고 조건문으로만 처리 가능(시작값보다 큰 인덱스의 값이 nums[idx:i]안에 들어있다면 이미 중복으로 path에 추가되었기 떄문에 continue)
                # if i > idx and nums[i] in nums[idx:i]:
                #     continue
                visited.add(nums[i])
                path.append(nums[i])
                backtracking(nums, i+1)
                path.pop()

        backtracking(nums, 0)
        return answer     