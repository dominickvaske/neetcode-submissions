# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def subtree(root1, root2):
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            
            return root1.val == root2.val and subtree(root1.left, root2.left) and subtree(root1.right, root2.right)
        
        def searchSubtree(root):
            if not root and not subRoot:
                return True
            elif not root:
                return False
            elif subtree(root, subRoot):
                return True
            else:
                return searchSubtree(root.left) or searchSubtree(root.right)
        
        return searchSubtree(root)



