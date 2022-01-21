from array2d import *


# we use None to show no path
def shortestpathfirst(w):
    n = w[0].numrows()
    q = w[0]
    r = w[1]
    for i in range(n):
        for j in range(n):
            if w[0][i, j] == 0:
                q[i, j] = None
    # print("Q 0")
    # q.traverse()
    # r.traverse()
    # print()
    for k in range(n):
        for i in range(n):
            if i == k:
                continue
            for j in range(n):
                if j == k:
                    continue
                oldval = q[i, j]
                q[i, j] = minimum(q[i, j], add(q[i, k], q[k, j]))
                if q[i, j] != oldval:
                    # cuts off the last letter of r[i.k] before appending to r[k,j]
                    r[i, j] = r[i, k][:-1] + r[k, j]
        # print("Q",k+1)
        # q.traverse()
        # r.traverse()
        # print()
    return [q, r]


def minimum(a, b):
    if a is None: return b
    if b is None: return a
    return min(a, b)


def add(a, b):
    if a is None: return None
    if b is None: return None
    return a + b


def weightmat(nodes, val):
    m = len(val)
    n = len(nodes)
    assert m == n ** 2
    w1 = Array2d(n, n)
    w2 = Array2d(n, n)
    w2.clear('-')
    k = 0
    for i in range(n):
        for j in range(n):
            w1[i, j] = val[k]
            if val[k] != 0:
                w2[i, j] = nodenames[i] + nodenames[j]
            k += 1
    return [w1, w2]


values = [7, 5, 0, 0, 7, 0, 0, 2, 0, 3, 0, 0, 4, 0, 1, 0]
nodenames = ['R', 'S', 'T', 'U']
w = weightmat(nodenames, values)
print("WEIGHT MATRIX")
w[0].traverse()
w[1].traverse()
print()
q = shortestpathfirst(w)
print("OUTPUT OF SHORTEST PATH ALGORITHM")
q[0].printcurrentstate()
q[1].printcurrentstate()
