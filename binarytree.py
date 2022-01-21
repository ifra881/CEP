class BTree:
    # creates tree root and returns a pointer to it.
    def __init__(self, item):
        self.data = item
        self.lc = None
        self.rc = None

    # adds item as left child to the node
    def addlc(self, item):
        assert self.lc is None, "Left child already present"
        self.lc = BTree(item)

    # adds item as right child to the node
    def addrc(self, item):
        assert self.rc is None, "Right child already present"
        self.rc = BTree(item)

    # deletes left child of node
    def dellc(self):
        assert self.lc is not None, "Left child absent"
        assert self.lc.lc is None and self.lc.rc is None, "This node has children"
        x = self.lc.data
        self.lc = None
        return x

    # deletes left child of node
    def delrc(self):
        assert self.rc is not None, "Right child absent"
        assert self.rc.lc is None and self.rc.rc is None, "This node has children"
        x = self.rc.data
        self.rc = None
        return x

    def traversein(self):
        if self.lc is not None:
            self.lc.traversein()
        print(self.data, end=" ")
        if self.rc is not None:
            self.rc.traversein()

    def traversebf(self):
        nodes = [self]
        print(self.data, end=" ")
        i=0
        n=1
        while i<n:
            p = nodes[i]
            if p.lc is not None:
                print(p.lc.data, end=" ")
                nodes.append(p.lc)
                n+=1
            if p.rc is not None:
                print(p.rc.data, end=" ")
                nodes.append(p.rc)
                n+=1
            i+=1
        print()

    def height(self):
        if self.rc is None and self.lc is None:
            return 1
        rh = 0
        lh = 0
        if self.rc is not None:
            rh = self.rc.height()
        if self.lc is not None:
            lh = self.lc.height()
        if rh > lh:
            return rh + 1
        return lh + 1

    def nodecount(self):
        if self.lc is None and self.rc is None:
            return 1
        lnc = 0
        rnc = 0
        if self.lc is not None:
            lnc = self.lc.nodecount()
        if self.rc is not None:
            rnc = self.rc.nodecount()
        return lnc + rnc + 1

    def leafcount(self):
        if self.lc is None and self.rc is None:
            return 1
        llc = 0
        rlc = 0
        if self.lc is not None:
            llc = self.lc.leafcount()
        if self.rc is not None:
            rlc = self.rc.leafcount()
        return llc + rlc

    def isStrictlyBinary(self):
        if self.lc is None:
            if self.rc is None:
                return True
            return False
        if self.rc is None:
            return False
        return self.lc.isStrictlyBinary() and self.rc.isStrictlyBinary()

    def isAlmostComplete(self):
        if self.isPerfect():
            return True
        if self.lc is None:
            return False
        hl = self.lc.height()
        if self.rc is None:
            if hl == 1:
                return True
            return False
        hr = self.rc.height()
        if hl == hr and self.lc.isPerfect():
            return self.rc.isAlmostComplete()
        if hl == hr + 1 and self.rc.isPerfect():
            return self.lc.isAlmostComplete()
        return False

    def isPerfect(self):
        h = self.height()
        n = self.nodecount()
        m = pow(2, h) - 1
        if n == m:
            return True
        return False
