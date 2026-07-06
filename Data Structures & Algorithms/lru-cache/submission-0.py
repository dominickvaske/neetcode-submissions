class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key
        self.nxt = None
        self.prv = None

class LRUCache:

    def __init__(self, capacity: int):
        # map keys to node
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)

        self.head.nxt = self.tail
        self.tail.prv = self.head

    def remove(self, node):
        prv, nxt = node.prv, node.nxt
        prv.nxt = nxt
        nxt.prv = prv

    def insert(self, node):
        nxtNode = self.head.nxt
        node.nxt = nxtNode
        nxtNode.prv = node
        self.head.nxt = node
        node.prv = self.head

    def get(self, key: int) -> int:
        # grab value and splice out to beginning
        if key in self.cache:
            resNode = self.cache[key]

            self.remove(resNode)
            self.insert(resNode)
        
            return resNode.val
        
        return -1 # if not in cache
  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) >= self.capacity:
            # remove the least recently used
            lru = self.tail.prv
            self.remove(lru)
            del self.cache[lru.key]
        
        newNode = ListNode(value, key)
        self.cache[key] = newNode
        self.insert(newNode)
