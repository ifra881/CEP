from binarytree import *


def build_bst(v):
    if len(v) == 0:
        return None
    root = BTree(v[0])
    for i in range(1, len(v)):
        root = addtobst(root, v[i])
    return root


def getsortedlist(node, v):
    if node.lc is not None:
        getsortedlist(node.lc, v)
    v.append(node.data)
    if node.rc is not None:
        getsortedlist(node.rc, v)
    # return v


def searchbst(node, target):
    if node is None: return [None, 0]
    if node.data == target: return [node, 1]
    if node.data > target:
        if node.lc is not None:
            if node.lc.data == target: return [node, 2]
            node = node.lc
        else: return [None, 0]
    else:
        if node.rc is not None:
            if node.rc.data == target: return [node, 3]
            node = node.rc
        else: return [None, 0]
    return searchbst(node, target)


def addtobst(root, item):
    assert root is not None
    parent = root
    added = False
    while added is False:
        #print("Parent carries", parent.data)
        if item == parent.data:
            added = True
            print(item, "has been already added")
        elif item < parent.data:
            if parent.lc is not None:
                parent = parent.lc
                #print("going left")
            else:
                parent.addlc(item)
                added = True
                #print(item, "added to left of", parent.data)
        else:
            if parent.rc is not None:
                parent = parent.rc
                #print("going right")
            else:
                parent.addrc(item)
                added = True
                #print(item, "added to right of", parent.data)
    return root



def delfrombst(root, item):
    x = searchbst(root, item)
    if x[0] is None: return root
    if x[1] == 1:
        #print("deleting root")
        if root.lc is None and root.rc is None: return None
        if root.lc is None and root.rc is not None: return root.rc
        if root.lc is not None and root.rc is None: return root.lc
        y = minimum(root.rc)
        if root.rc.data == y:
            root.rc.lc = root.lc
            root = root.rc
            return root
        z = searchbst(root.rc, y)
        z[0].lc = z[0].lc.rc
        root.data = y
        return root
    parvic = x[0]
    if x[1] == 2:
        #print("deleting left child")
        victim = x[0].lc
        if victim.lc is None and victim.rc is None:
            parvic.lc = None
            return root
        if victim.lc is None and victim.rc is not None:
            parvic.lc = victim.rc
            return root
        if victim.lc is not None and victim.rc is None:
            parvic.lc = victim.lc
            return root
        y = minimum(victim.rc)
        if victim.rc.data == y:
            victim.rc.lc = victim.lc
            parvic.lc = victim.rc
            return root
    if x[1] == 3:
        #print("deleting right child")
        victim = x[0].rc
        if victim.lc is None and victim.rc is None:
            parvic.rc = None
            return root
        if victim.lc is None and victim.rc is not None:
            parvic.rc = victim.rc
            return root
        if victim.lc is not None and victim.rc is None:
            parvic.rc = victim.lc
            return root
        y = minimum(victim.rc)
        if victim.rc.data == y:
            victim.rc.lc = victim.lc
            parvic.rc = victim.rc
            return root
    z = searchbst(victim.rc, y)
    z[0].lc = z[0].lc.rc
    victim.data = y
    return root