# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def diameter(root):
            nonlocal result
            if not root:
                return 0
            
            heightLeft = diameter(root.left)
            heightRight = diameter(root.right)

            result = max(result, heightLeft+heightRight)
            return max(heightLeft, heightRight) + 1
        
        diameter(root)
        return result





            
