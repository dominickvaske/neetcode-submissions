class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSymmetric(root1, root2):
            if not root2 and not root1:
                return True
            
            if not root1 or not root2 or root2.val != root1.val:
                return False
            
            return (isSymmetric(root1.left, root2.left) and 
                    isSymmetric(root1.right, root2.right))
        

        if not root:
            return False
            
        if root.val == subRoot.val:
            if isSymmetric(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)