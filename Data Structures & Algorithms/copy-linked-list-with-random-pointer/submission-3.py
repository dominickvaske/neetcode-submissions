class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copies = {}
        curr = head
        while curr:
            copies[curr] = Node(curr.val, None)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                copies[curr].next = copies[curr.next]
            if curr.random:
                copies[curr].random = copies[curr.random]
            curr = curr.next
        
        return copies[head]