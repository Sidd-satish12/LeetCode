# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_node = head
        slow_node = head

        if not head or not head.next or not head.next.next:
            return False
        
        while slow_node.next or fast_node.next:
            if not fast_node or not fast_node.next:
                return False
            fast_node = fast_node.next.next
            slow_node = slow_node.next

            if slow_node == fast_node:
                return True
        
        return False
