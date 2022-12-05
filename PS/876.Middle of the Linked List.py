# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_to_list = []
        temp = head
        while temp:
            node_to_list.append(head.val)
            temp = temp.next
        mid = len(node_to_list) // 2
        
        for _ in range(mid):
            head = head.next
        
        return head