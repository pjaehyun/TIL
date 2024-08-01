class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([int(detail[-4:-2]) for detail in details if int(detail[-4:-2]) > 60])