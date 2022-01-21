class qando:
    def __init__(self):
        self.q = []
        self.o = []
        self.f = None
        self.r = None

    def __len__(self):
        return len(q)

    def isEmpty(self):
        if self.f == None: return True
        if self.f > self.r: return True
        return False

    def enq(self, item, dequeued):
        self.q.append(item)
        if self.f == None:
            self.f = 0
            self.r = 0
        else:
            self.r += 1
        self.o.append(dequeued)

    def deq(self):
        if self.isEmpty(): return
        x = self.q[self.f]
        self.f += 1
        return x

    def readqando(self):
        i = self.r
        x = self.q[self.r]
        path = []
        while i >= 0 and x is not None:
            if self.q[i] == x:
                path.append(x)
                x = self.o[i]
            i -= 1
        path.reverse()
        return path

    def printcurrentstate(self):
        print("Q =", self.q, "F =", self.f, "R =", self.r)
        print("O =", self.o)
