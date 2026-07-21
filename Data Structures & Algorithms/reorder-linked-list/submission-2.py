class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
            
        nodeList = []
        curr = head
        while curr:
            nodeList.append(curr)
            curr = curr.next
        
        left, right = 0, len(nodeList)-1
        ptr = nodeList[left]
        left += 1
        while left <= right:
            if left <= right:
                ptr.next = nodeList[right]
                ptr = ptr.next
                right -= 1
            if left <= right:
                ptr.next = nodeList[left]
                ptr = ptr.next
                left += 1
        
        ptr.next = None