# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        def bfs(root):
            queue = deque([root])
            left = True
            output = []

            while queue:
                qLen = len(queue)
                temp = []
                for _ in range(qLen):
                    node = queue.popleft()
                    
                    temp.append(node.val)
                    
                    if node.left:
                        queue.append(node.left)
                    
                    if node.right:
                        queue.append(node.right)
                
                if left:
                    output.append(temp)
                else:
                    output.append(temp[::-1])
                left = not left

            return output

        return bfs(root)


