from queueforbfs import *
from stackwithlist import *


def bfs(nodes, adjlist, start, end):
    n=len(nodes)
    s= nodes[start]
    status = [1] * n
    myq = qando()
    myq.enq(start, None)
    status[s] = 2
    found = False
    while not myq.isEmpty() and not found:
        myq.printcurrentstate()
        x = myq.deq()
        if x==end:
            found=True
            break
        i=nodes[x]
        status[i] = 3
        for j in adjlist[x]:
            k=nodes[j]
            if status[k] == 1:
                myq.enq(j, x)
                status[k] = 2
    if found == False: return None
    myq.printcurrentstate()
    return myq.readqando()


def dfs(nodes, adjlist, start):
    n = len(nodes)
    s=nodes[start]
    status = [1] * n
    myst = mystack()
    myst.push(start)
    status[s] = 2
    nodeslist = []
    while not myst.isEmpty():
        #print(nodeslist)
        x = myst.pop()
        nodeslist.append(x)
        i=nodes[x]
        status[i] = 3
        for j in adjlist[x]:
            k = nodes[j]
            if status[k] == 1:
                myst.push(j)
                status[k] = 2
    #print(nodeslist)
    return nodeslist


def printpath(path, start, end):
    if path is None:
        print("No path found from",start,'to',end)
        return
    print('Printing path from', start, 'to', end, '...')
    for i in range(len(path) - 1):
        print(path[i], end=' -> ')
    print(path[-1])


def printnodes(nodeslist, start):
    if nodeslist is None:
        print("No node reachable from",start)
        return
    print('Printing list of nodes reachable from', start, '...')
    for i in range(len(nodeslist) - 1):
        print(nodeslist[i], end=', ')
    print(nodeslist[-1])


nodes = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6,'J':7, 'K':8}
adjlist={'A':'BCF', 'B':'CG', 'C':'F', 'D':'C', 'E':'CDJ', 'F':'D', 'G':'CE','J':'DK', 'K':'EG'}
start = 'A'
end = 'N'
print('Find a path from',start,'to',end,'using BFS')
path = bfs(nodes, adjlist, start, end)
printpath(path, start, end)
head = 'B'
print()
print('Find all nodes reachable from',head,'using DFS')
neighbours = dfs(nodes, adjlist, head)
printnodes(neighbours, head)