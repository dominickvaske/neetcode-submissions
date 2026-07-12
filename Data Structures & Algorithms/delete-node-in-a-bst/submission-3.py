# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSpot(root):
            if not root.left and not root.right:
                return root
            if not root.left:
                return root
            return findSpot(root.left)
            
        def searchNode(root):
            if not root:
                return root
            
            if root.val == key:
                if not root.left and not root.right:
                    return None
                if root.right: 
                    # find a root right node with a left opening
                    rightLeaf = findSpot(root.right)

                    # attach root.left to the left node as left.left
                    rightLeaf.left = root.left

                    # root = root.right
                    root = root.right
                else:
                    root = root.left
            
            if key < root.val:
                root.left = searchNode(root.left)
            else:
                root.right = searchNode(root.right)
            return root
        
        return searchNode(root)




        