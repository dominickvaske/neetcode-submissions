# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        tmp = l1
        step = 0
        num1 = 0
        while tmp:
            num1 += tmp.val * (10 ** step)
            step += 1
            tmp = tmp.next

        tmp = l2
        step = 0
        num2 = 0
        while tmp:
            num2 += tmp.val * (10 ** step)
            step += 1
            tmp = tmp.next
        
        total = num1 + num2

        if total == 0:
            return ListNode(0)

        prev = head = ListNode()
        while total > 0:
            digit = total % 10
            total = total // 10
            nxt = ListNode(digit)
            prev.next = nxt
            prev = nxt
        
        return head.next