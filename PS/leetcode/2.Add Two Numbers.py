# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = listNodeToNum(l1)
        num2 = listNodeToNum(l2)
        values = list(str(num1 + num2))
        values.reverse()
        lstNode = ListNode(values.pop(0))
        for v in values:
            lstNode = insertNode(lstNode, v)
        return lstNode
        
def insertNode(curr, val):
    if (curr == None):
        return ListNode(val)
    else:
        curr.next = insertNode(curr.next, val)
    return curr

def listNodeToNum(listNode):
        res = []
        while listNode != None:
            val = listNode.val
            listNode = listNode.next
            res.append(str(val))
        res.reverse()
        return int(''.join(res))