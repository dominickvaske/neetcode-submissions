# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def matches(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return matches(p.left,q.left) and matches(p.right,q.right)
        
        return matches(p,q)