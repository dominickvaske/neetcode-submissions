import sys
sys.setrecursionlimit(2000)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total_sum = 0

        def dfs(root):
            nonlocal total_sum

            if not root:
                return
            
            dfs(root.right)
            root.val += total_sum
            total_sum = root.val
            dfs(root.left)            
                    
        dfs(root)
        return root