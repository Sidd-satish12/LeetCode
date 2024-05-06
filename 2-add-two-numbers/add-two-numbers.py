# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        sum_list = ListNode()
        sum_list_beginning = sum_list
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            new_val = val1 + val2 + carry
            carry = new_val//10
            if carry:
                new_val = new_val % 10
            sum_list.val = new_val
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or carry:
                sum_list.next = ListNode()
                sum_list = sum_list.next
        return sum_list_beginning
