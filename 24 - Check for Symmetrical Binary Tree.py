# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        return root1.val == root2.val and self.solve(root1.left,root2.right) and self.solve(root2.left,root1.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.solve(root,root)
        
