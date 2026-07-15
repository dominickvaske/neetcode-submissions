class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        listLength = 1
        fast = head
        while fast.next:
            fast = fast.next
            listLength += 1
        
        dummy = ListNode(0,head)
        current = dummy
        for _ in range(listLength - n):
            current = current.next
        
        current.next = current.next.next

        return dummy.next