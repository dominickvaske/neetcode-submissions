# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        temp = l1
        while temp:
            num1.append(temp.val)
            temp = temp.next
        
        num2 = []
        temp = l2

        while temp:
            num2.append(temp.val)
            temp = temp.next
        
        num1Val = 0
        for i, num in enumerate(num1):
            num1Val += num * 10**i
        
        num2Val = 0
        for i, num in enumerate(num2):
            num2Val += num * 10**i
        
        # print(f"num1Val: {num1Val}, num2Val: {num2Val}")
        
        result = num1Val + num2Val
        head = ListNode(result % 10)
        result = result // 10
        temp = head
        while result:
            temp2 = ListNode(result % 10)
            temp.next = temp2
            temp = temp2
            result = result // 10
        
        return head


        
