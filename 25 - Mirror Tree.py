#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        if not root:
            return 
        if root:
            root.left ,root.right = root.right ,root.left
        self.mirror(root.left)
        self.mirror(root.right)
