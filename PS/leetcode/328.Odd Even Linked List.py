# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        even = None
        odd = None
        i = 1
        while head:
            if i % 2 == 0:
                even = insertNode(even,head.val)
            else:
                odd = insertNode(odd,head.val)
            head = head.next
            i += 1
        
        while even:
            odd = insertNode(odd, even.val)
            even = even.next
        return odd

    
    
def insertNode(curr, val):
    if (curr == None):
        return ListNode(val)
    else:
        curr.next = insertNode(curr.next, val)
    return curr