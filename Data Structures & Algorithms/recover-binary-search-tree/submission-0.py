# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []

        def inorder(root):
            nonlocal arr
            if not root:
                return

            inorder(root.left)
            arr.append(root)
            inorder(root.right)

        node1, node2 = None, None
        inorder(root)

        for i in range(len(arr)-1):
            if arr[i].val > arr[i+1].val:
                if node1 is None:
                    node1 = arr[i]
                node2 = arr[i+1]

        node1.val, node2.val = node2.val, node1.val

