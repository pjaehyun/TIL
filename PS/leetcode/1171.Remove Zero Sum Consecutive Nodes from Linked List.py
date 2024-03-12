# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        prefix_sum = 0
        prefix_sums = {0: temp}
        current = head

        while current:
            prefix_sum += current.val
            if prefix_sum in prefix_sums:
                deleted = prefix_sums[prefix_sum].next
                temp_sum = prefix_sum + deleted.val
                while deleted != current:
                    del prefix_sums[temp_sum]
                    deleted = deleted.next
                    temp_sum += deleted.val
                prefix_sums[prefix_sum].next = current.next
            else:
                prefix_sums[prefix_sum] = current
            current = current.next
        return temp.next
