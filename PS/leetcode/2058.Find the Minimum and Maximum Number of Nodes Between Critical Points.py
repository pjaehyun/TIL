# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        idxs = []
        min_value = float('inf')
        def dfs(head, prev, i):
            nonlocal min_value
            if not head:
                return

            if prev and head.next:
                if (head.val > prev.val and head.val > head.next.val) or (head.val < prev.val and head.val < head.next.val):
                    if idxs:
                        min_value = min(min_value, i - idxs[-1])
                    idxs.append(i)
            dfs(head.next, head, i+1)
        dfs(head, None, 1)
        
        return [-1, -1] if len(idxs) < 2 else [min_value, idxs[-1] - idxs[0]]