# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        combined = ListNode()
        tail = combined

        if list1 is None and list2 is None:
            return
        while True:
            if not list1:
                tail.next = list2
                break
            if not list2:
                tail.next = list1
                break
            
            if list1.val <= list2.val:
                tail.next = ListNode(list1.val)
                tail = tail.next
                list1 = list1.next
            else:
                tail.next = ListNode(list2.val)
                tail = tail.next
                list2 = list2.next
        return combined.next
        