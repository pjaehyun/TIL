# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 첫번째 풀이
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = nodeToList(head)
        lst.pop(len(lst) - n)
        if len(lst) <= 0:
            return
        listNode = ListNode(lst[0])
        
        for i in range(1, len(lst)):
            listNode = makeNode(listNode, lst[i])
        return listNode

def nodeToList(listNode):
    lst = []
    node = listNode
    while True:
        if node == None:
            return lst
        lst.append(node.val)
        node = node.next
        
def makeNode(listNode, n):
    if listNode == None:
        return ListNode(n)
    else:
        listNode.next = makeNode(listNode.next, n)
    return listNode

# 두번째 풀이
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next