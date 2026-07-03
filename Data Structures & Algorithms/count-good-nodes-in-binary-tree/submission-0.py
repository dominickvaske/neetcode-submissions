# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, maxSeenSoFar):
            nonlocal ans

            if not root:
                return
            
            if root.val >= maxSeenSoFar:
                ans += 1
        
            dfs(root.left, max(maxSeenSoFar, root.val))
            dfs(root.right, max(maxSeenSoFar, root.val))

        dfs(root, root.val)
        return ans

            
            