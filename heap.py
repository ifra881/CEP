class heap:
    def __init__(self):
        self.hlist = []

    def __len__(self):
        return len(self.hlist)

    def isEmpty(self):
        return len(self) == 0

    def rise(self):
        if len(self) <= 1: return
        # heap contains more than one elements
        # start with the last element
        index = len(self) - 1
        p = (index - 1) // 2
        while p >= 0:
            # parent exists
            if self.hlist[index] <= self.hlist[p]:
                return
            self.swap(index,p)
            index = p
            p = (index - 1) // 2

    def add_to_heap(self, item):
        self.hlist.append(item)
        self.rise()

    def sink(self,lenheap):
        if lenheap <= 1: return
        # heap contains more than one elements
        # start with the root
        index = 0
        lc = 2 * index + 1
        while lc < lenheap:
            # left child exists
            if lc == (lenheap - 1):
                # there is no right child, we have reached end of heap
                if self.hlist[lc] > self.hlist[index]:
                    self.swap(lc,index)
                return
            rc = lc + 1
            if rc < lenheap:
                # right child exists
                if self.hlist[lc] <= self.hlist[index] and self.hlist[rc] <= self.hlist[index]:
                    return
                if self.hlist[lc] >= self.hlist[rc]:
                    self.swap(lc,index)
                    index = lc
                else:
                    self.swap(rc,index)
                    index = rc
                lc = 2 * index + 1

    def del_from_heap(self):
        assert not self.isEmpty(), "Underflow"
        x = self.hlist[0]
        if len(self) > 1:
            self.hlist[0] = self.hlist.pop()
            self.sink(len(self))
        else:
            self.hlist = []
            self.len = 0
        return x

    def traverse(self):
        print(self.hlist)

    def swap(self,x,y):
        self.hlist[x],self.hlist[y]=self.hlist[y],self.hlist[x]

    def furnishlist(self):
        return self.hlist
