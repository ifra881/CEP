from heap import heap


def buildheap(val):
    h = heap()
    for i in range(len(val)):
        h.add_to_heap(val[i])
    return h


def heapsort(val):
    myheap = buildheap(val)
    n = len(myheap)
    for i in range(n-1):
        myheap.swap(0, n - 1 - i)
        myheap.sink(n - 1 - i)
    # even though it is a heap object, it DOES NOT contain a max heap now.
    return myheap.furnishlist()


values = [3, 7, 8, 9, 10, 12, 9, 2, 5]
heap1 = buildheap(values)
heap1.traverse()
# y = heap1.delfromheap()
# print(y)
# heap1.traverse()
x = 11
heap1.add_to_heap(x)
print("After adding", x)
heap1.traverse()
while not heap1.isEmpty():
    print(heap1.del_from_heap())
listtosort = [51, 23, 67, 87, 12, 100, 84, 71, 60, 23, 12, 29, 1, 37, 4, 90]
heap2=buildheap(listtosort)
heap2.traverse()
#listtosort=[10,9,8,7,6,5,4,3,2,1]
#listtosort=[1,2,3,4,5,6,7,8,9,10]
print("sorting")
heap2list = heapsort(listtosort)
print(heap2list)
