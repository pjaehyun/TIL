# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev = head
        while prev:
            while prev.next and prev.next.val == val:
                prev.next = prev.next.next
            prev = prev.next
        
        if head and head.val == val:
            head = head.next
        return head