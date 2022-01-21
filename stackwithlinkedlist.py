from singlylinkedlist import ListNode

class mystack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def pop(self):
        assert not self.isEmpty(),"Empty stack"
        x = self.top.data
        self.top = self.top.next
        return x

    def push(self,val):
        x = ListNode(val)
        x.next = self.top
        self.top = x

