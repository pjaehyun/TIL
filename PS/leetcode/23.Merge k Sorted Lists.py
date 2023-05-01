# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hq = []

        for i in range(len(lists)):
            temp = lists[i]
            while temp:
                heapq.heappush(hq, temp.val)
                temp = temp.next
        if hq:
            answer = ListNode(heapq.heappop(hq))
            temp = answer
            while hq:
                node = ListNode(heapq.heappop(hq))
                temp.next = node
                temp = temp.next
            return answer