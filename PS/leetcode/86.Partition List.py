# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def insert(node, val):
            temp = node
            while temp.next:
                temp = temp.next
            temp.next = val
            
        partition1 = ListNode()
        partition2 = ListNode()

        while head:
            if head.val < x:
                insert(partition1, ListNode(head.val))
            else:
                insert(partition2, ListNode(head.val))
            head = head.next
        insert(partition1, partition2.next)
        
        return partition1.next