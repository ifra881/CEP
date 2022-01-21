class mystack:
    def __init__(self):
        self.elements = list()

    def isEmpty(self):
        return len(self.elements) == 0

    def pop(self):
        assert not self.isEmpty(),"Empty stack!"
        x = self.elements.pop()
        #self.top -= 1
        return x

    def push(self,value):
        #self.top += 1
        self.elements.append(value)


