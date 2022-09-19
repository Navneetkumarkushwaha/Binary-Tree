# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        if not root:
            return ans
        left_right = True
        q = [root]
        
        while q:
            
            n = len(q)
            temp = []
            for _ in range(n):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if left_right:
                ans.append(temp)
            else:
                temp.reverse()
                ans.append(temp)
            left_right = not left_right
        
        return ans
        
 Time Complexity: O(N)   

Space Complexity: O(N)
