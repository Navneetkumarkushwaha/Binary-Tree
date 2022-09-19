#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
   
   def printLeaves(self, root):
       if(root):
           self.printLeaves(root.left)
           if root.left is None and root.right is None:
               self.result.append(root.data)
           self.printLeaves(root.right)
   
   def printBoundaryLeft(self,root):
       if(root):
           if (root.left):
               # to ensure top down order, print the node
               # before calling itself for left subtree
               self.result.append(root.data)
               self.printBoundaryLeft(root.left)
           elif(root.right):
               self.result.append(root.data)
               self.printBoundaryLeft(root.right)
           # do nothing if it is a leaf node, this way we
           # avoid duplicates in output
   # A function to print all right boundary nodes, except
   # a leaf node. Print the nodes in BOTTOM UP manner
   
   def printBoundaryRight(self,root):
       if(root):
           if (root.right):
               # to ensure bottom up order, first call for
               # right subtree, then print this node
               self.printBoundaryRight(root.right)
               self.result.append(root.data)
           elif(root.left):
               self.printBoundaryRight(root.left)
               self.result.append(root.data)
           # do nothing if it is a leaf node, this way we 
           # avoid duplicates in output
   # A function to do boundary traversal of a given binary tree
   
   def printBoundaryView(self,root):
       self.result = []
       if (root):
           self.result.append(root.data)
           # Print the left boundary in top-down manner
           self.printBoundaryLeft(root.left)
           # Print all leaf nodes
           self.printLeaves(root.left)
           self.printLeaves(root.right)
           # Print the right boundary in bottom-up manner
           self.printBoundaryRight(root.right)
       return self.result
