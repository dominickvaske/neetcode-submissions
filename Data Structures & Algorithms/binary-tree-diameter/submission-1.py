# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = 0

        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            heightL = dfs(root.left)
            heightR = dfs(root.right)

            maxDiameter = max(maxDiameter, heightL + heightR)

            return 1 + max(heightR, heightL) 
        
        dfs(root)
        return maxDiameter

#    1
#   2 4
#  3