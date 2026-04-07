class ListNode:
    
    def __init__(self,key, val):
        self.key=key
        self.value=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.mydir={}
        self.left=ListNode(0,0)
        self.right=ListNode(0,0)
        self.left.next=self.right
        self.right.prev=self.left

    def rightinsert(self, Node: ListNode)->None:
        previous=self.right.prev
        previous.next=Node
        Node.prev=previous
        Node.next=self.right
        self.right.prev=Node

    def delete(self, Node : ListNode)->None:
        #del self.mydir[Node.key]
        previous=Node.prev
        after=Node.next
        Node.prev, Node.next=None,None
        previous.next, after.prev = after, previous

    def get(self, key: int) -> int:
        if key in self.mydir:
            self.delete(self.mydir[key])
            self.rightinsert(self.mydir[key])
            return self.mydir[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if key in self.mydir:
            node = self.mydir[key]
            node.value = value
            self.delete(node)
            self.rightinsert(node)
        else:
            if len(self.mydir) == self.cap:
                lru = self.left.next
                self.delete(lru)
                del self.mydir[lru.key]

            node = ListNode(key, value)
            self.mydir[key] = node
            self.rightinsert(node)
