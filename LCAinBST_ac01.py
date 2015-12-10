__author__ = 'chi'


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# !/usr/bin/env python
# -*- coding : utf-8 -*-

class Node:
    def __init__(self, val, root,left, right):
        self.val = val
        self.root = root
        self.left = left
        self.right = right

class BinaryTree:

    def __init__(self, root = None):
        self.root = root

    def create(self, pList):
        self.root = Node(pList[0],None,None, None)

        for i in pList[1:]:
            self.insert (i, self.root)

    def insert(self,val,root_node = None):
        if root_node.val == val:
            return
        if root_node.val > val:
            if root_node.left is None:
                root_node.left = Node(val, root_node, None, None)
            else:
                return self.insert( val,root_node.left)
        if root_node.val < val:
            if root_node.right is None:
                root_node.right = Node(val, root_node, None, None)
            else:
                return self.insert( val,root_node.right)
#plist = [6,2,8,0,4,7,9,3,5]
plist=[2,1,3,0,5]
myBT = BinaryTree()
myBT.create(plist)


root = myBT.root

qval = 0

pval = 1

recordp = []
recordq = []

tmpq = root
while tmpq:
    recordq.append(tmpq)
    if qval == tmpq.val:
        break
    elif qval < tmpq.val:
        tmpq = tmpq.left
    else:
        tmpq = tmpq.right

tmpp = root

while tmpp:
    recordp.append(tmpp)
    if pval == tmpp.val:

        break
    elif pval < tmpp.val:
        tmpp = tmpp.left
    else:
        tmpp = tmpp.right

i=0
mini = min(len(recordq),len(recordp))
while recordq[i] == recordp[i] and i < mini-1:
    i+=1

if recordp[i] == recordq[i]:
    tt = i
else:
    tt = i-1

print(qval,pval)
print(recordq[tt].val)


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        recordp = []
        recordq = []

        pval=p.val
        qval=q.val
        tmpq = root
        while tmpq:
            recordq.append(tmpq)
            if qval == tmpq.val:
                break
            elif qval < tmpq.val:
                tmpq = tmpq.left
            else:
                tmpq = tmpq.right

        tmpp = root
        while tmpq:
            recordp.append(tmpp)
            if pval == tmpp.val:
                break
            elif pval < tmpp.val:
                tmpp = tmpp.left
            else:
                tmpp = tmpp.right

        i=0
        mini = min(len(recordq),len(recordp))
        while recordq[i] == recordp[i] and i < mini-1:
            i+=1

        if recordp[i] == recordq[i]:
            tt = i
        else:
            tt = i-1
        return recordp[tt]

"""