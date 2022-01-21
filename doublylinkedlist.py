class DLNode:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

    def __len__(self):
        a = self
        i = 0
        while a is not None:
            i += 1
            a = a.right
        a = self.left
        while a is not None:
            i += 1
            a = a.left
        return i

    def insertright(self,value):
        #p  q   r
        p = self
        q = DLNode(value)
        r = p.right
        q.right = r
        q.left = p
        p.right = q
        if r is not None:
            r.left=q

    def insertleft(self,value):
        #r  q   p
        p=self
        q = DLNode(value)
        r = p.left
        q.left = r
        q.right = p
        p.left = q
        if r is not None:
            r.right=q

    def delete(self):
        #p  q   r
        p = self.left
        q = self
        r = self.right
        if p is not None:
            p.right = r
        if r is not None:
            r.left = p
        if p is None:
            return r
        return p

    def traverse(self):
        a = self
        i=0
        #go all the way back to the start
        while a.left is not None:
            a = a.left
        #now go all the way to the end
        print("Traversing...")
        while a is not None:
            print(a.data,end=" ")
            a = a.right
        print()

    def search(self,target):
        b=self
        #check the nodes on the right
        while b is not None and b.data!=target:
            b=b.right
        if  b is not None:
            return b
        # check the nodes on the left
        b=self.left
        while b is not None and b.data!=target:
            b=b.left
        return b
