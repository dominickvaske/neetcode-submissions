# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy_head = ListNode(0, head)
        pre = dummy_head
        for _ in range(left - 1):
            pre = pre.next
        
        lNode = pre.next
        rNode = lNode
        for _ in range(right - left):
            rNode = rNode.next
        
        after = rNode.next
        curr = lNode
        prev = after
        
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        pre.next = prev
        return dummy_head.next
