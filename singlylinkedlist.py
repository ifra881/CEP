class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def traverse(self):
        a=self
        print("Traversing the list...")
        while a is not None:
            print(a.data,end=" ")
            a=a.next

    def __len__(self):
        a = self
        i=0
        while a is not None:
            i+=1
            a = a.next
        return i

    def insert(self, value):
        n = ListNode(value)
        n.next=self.next
        self.next=n

    def delete(self):
        item=None
        if self.next is not None:
            tmp=self.next
            item=tmp.data
            self.next=tmp.next
        return item

    def search(self,target):
        a=self
        if a.data==target:
            return [True, None, a]
        b=a.next
        while b is not None and b.data!=target:
            a=a.next
            b=b.next
        return [b is not None, a, b]

    def circularize(self):
        a=self
        while a.next is not None:
            a=a.next
        a.next=self

    def traverse_circular(self):
        a = self
        print("Traversing the list...")
        while a.next is not self:
            print(a.data, end=" ")
            a = a.next
        print(a.data, end=" ")
        print()

    def linearize(self):
        a = self
        while a.next is not self:
            a = a.next
        a.next = None

