# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            
            heightLeft = dfs(root.left)
            heightRight = dfs(root.right)

            if abs(heightLeft - heightRight) > 1:
                res = False
            
            return max(heightLeft, heightRight) + 1
        
        dfs(root)
        return res



