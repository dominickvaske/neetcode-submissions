# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        output = []

        def bfs(root):
            queue = deque([root])

            while queue:
                qLength = len(queue)
                output.append(queue[-1].val)

                for _ in range(qLength):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        
        bfs(root)
        return output