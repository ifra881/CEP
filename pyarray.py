import ctypes


class Array:
    def __init__(self, n):
        assert n > 0, 'Array size must be > 0'
        self.size = n
        self.elements = (ctypes.py_object * n)()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Invalid index"
        return self.elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Invalid index"
        self.elements[index] = value

    def insert(self, index, value):
        for i in range(self.size - 1, index, -1):
            self.elements[i] = self.elements[i-1]
        self.elements[index] = value

    def delete(self, index):
        for i in range(index, self.size-1, 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.size-1] = None

    def traverse(self):
        for i in range(len(self)):
            print(self.elements[i], end=" ")
        print()

    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value


myarray=Array(12)
print("We create an array of 12 elements")
myarray.traverse()
for i in range(8):
    myarray[i]=i+2
print("this is how it looks...")
myarray.traverse()
print("x=", myarray[3])
myarray.delete(2)
print("after deleting at 2...")
myarray.traverse()
myarray.insert(5, 1)
print("after inserting 1 at 5...")
myarray.traverse()