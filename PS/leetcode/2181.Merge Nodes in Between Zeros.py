# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        temp = answer
        def dfs(head, _sum):
            nonlocal temp, answer
            if not head:
                return
            
            if head.val == 0 and _sum > 0:
                temp.next = ListNode(_sum)
                temp = temp.next
                _sum = 0
            
            dfs(head.next, _sum + head.val)
        dfs(head, 0)
        return answer.next